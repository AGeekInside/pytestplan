import socket
import sys

HOSTNAME = socket.gethostname().lower().split('.')[0].replace('-', '')
print("HOSTNAME = %s" % HOSTNAME)



try:
    exec "from host_%s import *" % HOSTNAME
    print("imported host_%s" % HOSTNAME)
    print("proj_dir = %s" % proj_dir)
except ImportError, e:
    e = sys.exc_info()[0]
    #print("Error: %s" % e)
    #print("Failed to import host_%s" % HOSTNAME)
    pass

try:
    from local import *
except ImportError, e:
    # e = sys.exc_info()[0]
    # print("Error: %s" % e)
    # print("Failed to import local")
    pass
