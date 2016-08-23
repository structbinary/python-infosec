import os

def child_process():
    print("I am the child process with pid %d") %os.getpid()

def parent_process():
    print "I am  parent process with pid %d" %os.getpid()
    print "going to create a child process"
    child_pid = os.fork()
    if child_pid == 0:
        # we are inside child
        child_process()
    else:
        print "we are inside the parent process"
        print "our child has pid %d" %child_pid

parent_process()