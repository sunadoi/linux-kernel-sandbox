#!/usr/bin/python3
import os, sys
ret = os.fork()
if ret == 0:
    print("child process: pid={}, parent process pid={}".format(os.getpid(), os.getppid()))
    exit()
elif ret > 0:
    print("parent process: pid={}, child process pid={}".format(os.getpid(), ret))
    exit()
sys.exit(1)