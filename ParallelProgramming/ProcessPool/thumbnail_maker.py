import time
import os
import logging
from urllib.parse import urlparse
from urllib.request import urlretrieve

from queue import Queue
from threading import Thread
 
import multiprocessing

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

        #img_list will contain list of downloaded files,i.e. their names and will be served to process pool
        self.img_list = []

        #dl_queue will handle the threads which we will use to parallely download the images


    #function to download 1 image at a time, made to be used by single thread
    def download_image(self, dl_queue):
        #running loop till there are urls in the dl_queue
        while not dl_queue.empty():
            """
            If we call get function on an empty queue with block=False, it will generate an exception, hence try block.
            Even though we are running a loop until dl_queue is not empty, one thread might get the last value from queue,
            and another thread might be in the loop simultaneously, and can raise this empty queue exception.
            """
            try:
                url = dl_queue.get(block=False)

                # download each image and save to the input dir
                img_filename = urlparse(url).path.split('/')[-1]
                urlretrieve(url, self.input_dir + os.path.sep + img_filename)
                self.img_list.append(img_filename)

                #mark the task done for each image downloaded
                dl_queue.task_done()
            except Queue.empty:
                logging.info("Queue empty!")

    def resize_image(self, filename):
        target_sizes = [32, 64, 200]
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

    def make_thumbnails(self, img_url_list):
        logging.info("START make_thumbnails")

        #creating a pool of processes, by default it no.of processes created will be equal to cores in processor
        pool = multiprocessing.Pool()

        #storing start time
        start = time.perf_counter()

        dl_queue = Queue()
        #adding each url in download queue
        for img_url in img_url_list:
            dl_queue.put(img_url)

        #limiting no.of threads to be created, and not allowing 1 thread per url which can become resource intensive
        num_dl_threads = 4

        for _ in range(num_dl_threads):
            t = Thread(target=self.download_image,args=(dl_queue,))
            t.start()

        dl_queue.join()
        
        start_resize = time.perf_counter()
        pool.map(self.resize_image,self.img_list)
        end_resize = time.perf_counter()

        #storing end time of download and resize operations
        end = time.perf_counter()

        pool.close()
        pool.join()
        logging.info("created {}  thumbnails in {} seconds".format(len(self.img_list),end_resize-start_resize))
        logging.info("END make_thumbnails in {} seconds".format(end - start))
