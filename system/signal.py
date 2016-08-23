import signal

def cntl_hanlder(signum, frm):

    print "Haha! You can not kill me"

print "Installing Signal Haldler"
signal.signal(signal.SIGINT, cntl_hanlder)
print "Done"
while True:
    pass

#Create a Tcp server which listen on port
#implement signal to ensure it automatically shuts down after a pre-configured duration,which is given by command line
#eg tcp-server -s 100
#shutsdown after listening to port for 100 seconds
#hint- use sigalarm to solve this problem