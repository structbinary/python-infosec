import threading
import Queue
import time
from ftplib import FTP
import os

"""
Create a list of FTP sites
Create a worker thread which can login to these sites and list the root directory and exit
No. of worker thread to be used = 5
No. of FTP sites = 10
"""

class workerThread(threading.Thread):

    def __init__(self, queue, id):
        threading.Thread.__init__(self)
        self.queue = queue
        self.tid = id

    def run(self):
        print "In worker thread"
        while True:
            try:
                host = self.queue.get()
            except Queue.Empty:
                print "Worker %d exiting" % (self.tid)
                return
            try:
                ftp = FTP(host)
                ftp.login()
                print "listing files in root directory"
                files = ftp.dir()
                directory = "/"
                filematch = '*'
                ftp.cwd(directory)
                for filename in ftp.nlst(filematch):
                    print 'Getting ' + filename
            except Exception as e:
                print e
            self.queue.task_done()


queue = Queue.Queue()
def main():
    for id in range(5):
        print "creating workerThread : %d" % id
        worker = workerThread(queue, id)
        worker.setDaemon(True)
        worker.start()
        print "WorkerThread %d created" % id

    with open('ftp_server.list') as f:
        for eachline in f:
            server_name = eachline.strip('\n')
            queue.put(server_name)

    queue.join()
    print "All task over !!"

main()

