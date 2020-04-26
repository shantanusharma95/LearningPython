import time
import os
import logging
from urllib.parse import urlparse
from urllib.request import urlretrieve
import threading

import PIL
from PIL import Image

"""specifying format to see the log messages to include -
threadname, current times, logging level and the message"""
FORMAT = "[%(threadName)s, %(asctime)s, %(levelname)s] %(message)s"
logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format=FORMAT)

class ThumbnailMakerService(object):
    def __init__(self, home_dir='.'):
        self.home_dir = home_dir
        self.input_dir = self.home_dir + os.path.sep + 'incoming'
        self.output_dir = self.home_dir + os.path.sep + 'outgoing'
        self.downloaded_bytes = 0
        self.dl_lock = threading.Lock()

    # download single image available at the url received 
    def download_image(self, url):
        logging.info("downloading image at URL ",url)
        img_filename = urlparse(url).path.split('/')[-1]
        dest_path = self.input_dir + os.path.sep + img_filename
        urlretrieve(url, dest_path)

        #get size of downloaded image
        img_size =  os.path.getsize(dest_path)

        """Here we are locking the shared variable downloaded_bytes, which stores total size of all images downloaded.
        We want it to be updated by each thread only after fetching the correct and updated value, and dont want multiple
        threads to read the same value and update it, which will give out incorrect output."""

        """Also, we use the thread lock in a WITH block so that even in case of an exception, the lock is released once 
        control passes out of the WITH block.
        The same could have been achieved by using try-catch and having the lock released in finally block"""
        with self.dl_lock:
            self.download_bytes+=img_size
        logging.info("Image [{} bytes] saved to {}".format(img_size,dest_path))

    #function to download images
    def download_images(self, img_url_list):
        # validate inputs
        if not img_url_list:
            return

        #creating directory to store downloaded images
        os.makedirs(self.input_dir, exist_ok=True)
        
        logging.info("beginning image downloads")

        start = time.perf_counter()

        #creating a list to hold all threads created, so they can then be joined together after each is started
        threads = [] 

        #creating many worker threads, which will then start in the loop calling the download_image function
        for url in img_url_list:
            t = threading.Thread(target=self.download_image, args=(url,))
            t.start()
            threads.append(t)

        """after all the threads are created and started, they are appended to a list.
        Now each thread will be joined, so that the main thread is forced to wait for all threads to complete"""
        for t in threads:
            t.join()

        end = time.perf_counter()

        logging.info("downloaded {} images in {} seconds".format(len(img_url_list), end - start))

    #function to perform resizing on images
    def perform_resizing(self):
        # validate inputs
        if not os.listdir(self.input_dir):
            return

        #creating directory to store resized images
        os.makedirs(self.output_dir, exist_ok=True)

        logging.info("beginning image resizing")
        target_sizes = [32, 64, 200]
        num_images = len(os.listdir(self.input_dir))

        start = time.perf_counter()
        for filename in os.listdir(self.input_dir):
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
        end = time.perf_counter()

        logging.info("created {} thumbnails in {} seconds".format(num_images, end - start))

    def make_thumbnails(self, img_url_list):
        logging.info("START make_thumbnails")

        #storing start time
        start = time.perf_counter()

        self.download_images(img_url_list)
        self.perform_resizing()

        #storing end time of download and resize operations
        end = time.perf_counter()
        logging.info("END make_thumbnails in {} seconds".format(end - start))
