Under this directory, I have placed more directories. Each directory contains the code files along with an output log, where the time
taken to run the program is recorded to depict the differences between serial and parallel program - also note, the code is doing the 
same thing in all cases.

I have purposely uploaded my output logs - they can differ based on system configuration. I would recommend executing the code in a Python
virtual environment. As I personally use Microsoft Visual Studio, below is the guide to begin with virtual environment on the same-
https://code.visualstudio.com/docs/python/environments 

To run the code, save all python files, and under test_thumbnail_maker.py, run ">pytest"
The above file is common under all sub-directories, but I have still kept it in each of those for the purpose of ease of using and if I 
need to make changes to some of those in future.

Below is a summary of what each sub-directory contains.

  - ##### SerialRun
    * Contains the code which is executed serially. All the images are downloaded one by one, one after the another - then each
    image is resized one after the another.
    
  - ##### MultipleThread
    * Here I have used the "threading" module, and multiple threads are created, one for each image. 
  
    * As I am downloading and resizing very limited no.of images, i.e. 26, it is ok to create the same no.of threads. But had the no.of
    images been a lot, say more than 100, this approach would be really bad as CPU will allocate resources to so many threads and at 
    some point, all resources can be exhausted and system can get stuck!
    
    * I have also implemented thread lock. As all threads can randomly access shared resources of a process, I have used the locking
    mechanism so that only 1 thread can access and update a shared resource - this way, each thread will update the correct shared
    resource value.
   
  - ##### MultipleThreadsInLimit
    * In this, I have limited the threads to 4 only for downloading purpose, i.e. instead of a new thread for 
    downloading form each URL, now we will have only 4 threads downloading all the images, unlike done in the MultipleThread directory.
    
    * This gives us control over how many threads are active and keeps the CPU utilization within limits in case the no.of URLs increases.
    
    * Also, in this I use Queue - following the producer consumer concept. The use of thread locks was avoided as Queue internally 
    handles thread synchronization. However, there were some minor but important checks, which I have explained in the code comments.
    
  - ##### ProcessPool
    * Here I make use of multiple processes via process pool to do the resizing of images parallely.
    * The time taken to resize the images is considerably reduced as compared to the previous approaches - this can be noted in the 
      logfile.
