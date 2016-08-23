import threading
import Queue
import time

class workerThread(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        print "In worker thread"
        while True:
            counter = self.queue.get()
            print "Order to sleep for %d  seconds" %counter
            time.sleep(counter)
            print "Finished sleeping for %d seconds" %counter
            self.queue.task_done()


queue = Queue.Queue()

for i in range(10):
    print "creating workerThread : %d" %i
    worker = workerThread(queue)
    worker.setDaemon(True)
    worker.start()
    print "WorkerThread %d created" %i


for j in range(10):
    queue.put(j)

queue.join()
print "All task over !!"

#Exercise
# Create a list of FTP sites
#Create a worker thread and queues which can login to these sites and list the root directory and exit
#Use 5 threads for this job and 10 ftp sites

#Write python script showing how you can create locking mechanism with the shared resources using the thread module
#Investigate about multiprocessing module and write a TCP SYN scanner using multiprocessing