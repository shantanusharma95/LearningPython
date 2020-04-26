import time
import os
import logging
from urllib.parse import urlparse
from urllib.request import urlretrieve

from queue import Queue
from threading import Thread

import PIL
from PIL import Image

#Using queue here, similar to consumer-producer concept

FORMAT = "[%(threadName)s, %(asctime)s, %(levelname)s] %(message)s"
logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format = FORMAT)

class ThumbnailMakerService(object):
    def __init__(self, home_dir='.'):
        self.home_dir = home_dir
        self.input_dir = self.home_dir + os.path.sep + 'incoming'
        self.output_dir = self.home_dir + os.path.sep + 'outgoing'

        #img_queue will handle the queue for downloading and resizing threads, i.e. 2 threads only
        self.img_queue = Queue()

        #dl_queue will handle the threads which we will use to parallely download the images
        self.dl_queue = Queue()

    #function to download 1 image at a time, made to be used by single thread
    def download_image(self):
        #running loop till there are urls in the dl_queue
        while not self.dl_queue.empty():
            """
            If we call get function on an empty queue with block=False, it will generate an exception, hence try block.
            Even though we are running a loop until dl_queue is not empty, one thread might get the last value from queue,
            and another thread might be in the loop simultaneously, and can raise this empty queue exception.
            """
            try:
                url = self.dl_queue.get(block=False)

                # download each image and save to the input dir
                img_filename = urlparse(url).path.split('/')[-1]
                urlretrieve(url, self.input_dir + os.path.sep + img_filename)
                self.img_queue.put(img_filename)

                #mark the task done for each image downloaded
                self.dl_queue.task_done()
            except Queue.empty:
                logging.info("Queue empty!")

    #function to perform resizing on images
    def perform_resizing(self):
        # validate inputs
        
        #creating directory to store resized images
        os.makedirs(self.output_dir, exist_ok=True)

        logging.info("beginning image resizing")
        target_sizes = [32, 64, 200]
        num_images = len(os.listdir(self.input_dir))

        start = time.perf_counter()
        while True:
            """
            After downloading all images, we added None to the queue.
            The below condition will check if the filename is None,i.e. when the None item is read,
            it will no there are no more items in the queue and the loop will break.
            """
            if filename:
                filename = self.img_queue.get()
                logging.info("resizing image {} ".format(filename))
                orig_img = Image.open(self.input_dir + os.path.sep + filename)
                for basewidth in target_sizes:
                    img = orig_img
                    # calculate target height of the resized image to maintain the aspect ratio
                    wpercent = (basewidth / float(img.size[0]))
                    hsize = int((float(img.size[1]) * float(wpercent)))
                    # perform resizing
                    img = img.resize((basewidth, hsize), PIL.Image.LANCZOS)
                    
                    # save the resized image to the output dir with a modified file name 
                    new_filename = os.path.splitext(filename)[0] + \
                        '_' + str(basewidth) + os.path.splitext(filename)[1]
                    img.save(self.output_dir + os.path.sep + new_filename)

                os.remove(self.input_dir + os.path.sep + filename)
                logging.info("done resizing image {} ".format(filename))
                self.img_queue.task_done()
            else:
                self.img_queue.task_done()
                break
        end = time.perf_counter()

        logging.info("created {} thumbnails in {} seconds".format(num_images, end - start))

    def make_thumbnails(self, img_url_list):
        logging.info("START make_thumbnails")

        #storing start time
        start = time.perf_counter()

        #adding each url in download queue
        for img_url in img_url_list:
            self.dl_queue.put(img_url)

        #limiting no.of threads to be created, and not allowing 1 thread per url which can become resource intensive
        num_dl_threads = 4

        for _ in range(num_dl_threads):
            t = Thread(target=self.download_image)
            t.start()

        """
        Here, we will not join the threads in the above loop, else any 1 thread completing will notify resizing thread to begin,
        while others are still downloading.
        So, we use dl_queue.join() to ensure all threads in above loop complete their downloads before dl_queue is marked done.
        Then put the None value in img_queue, so resizing thread will know that there are no images left in queue for resizing.
        """
        t2 = Thread(target=self.perform_resizing)
        t2.start()

        self.dl_queue.join()
        self.img_queue.put(None)
        t2.join()

        #storing end time of download and resize operations
        end = time.perf_counter()
        logging.info("END make_thumbnails in {} seconds".format(end - start))
