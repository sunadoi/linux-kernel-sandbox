#!/usr/bin/python3
import os
os.posix_spawn("/bin/echo", ["echo", "echo", "posix_spawn()"], {})
print("generate echo command")