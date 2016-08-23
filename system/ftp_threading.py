import threading
import Queue
import time
from ftplib import FTP
import os



class workerThread(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        print "In worker thread"
        while True:
            host = self.queue.get()
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


queue = Queue.Queue
def main():

    for i in range(5):
        print "creating workerThread : %d" % i
        worker = workerThread(queue)
        worker.setDaemon(True)
        worker.start()
        print "WorkerThread %d created" % i

    with open('ftp_server.list') as f:
        for eachline in f:
            server_name = eachline.strip('\n')
            queue.put(server_name)

    queue.join()
    print "All task over !!"

main()

