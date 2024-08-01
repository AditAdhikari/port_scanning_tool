import socket
import sys
import time
import threading

usage ="python3 scanning_tool.py TARGET START_PORT END_PORT"

START_TIME = time.time()

if(len(sys.argv) != 4):
    print(usage)
    sys.exit()

try:
    target = socket.gethostname(sys.argv[1])
except socket.gaierror:
    print("name resolution error")
    sys.exit()

START_PORT = int(sys.argv[2])
END_PORT = int(sys.argv[3])

print("scanning wait.... \n")

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((target, port))
    if(not conn):
        print("port {} is OPEN".format(port))
    s.close()

for port in range(START_PORT,END_PORT+1):

    thread = threading.Thread(target= scan_port, args=(port,))
    thread.start()

END_TIME = time.time()

print("time takes to scan: ", END_TIME - START_TIME,'s')