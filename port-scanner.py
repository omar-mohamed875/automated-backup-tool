#!/usr/bin/python3
# port scanner project

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("invalid choice")
    sys.exit()

print("-" * 50)
print("your ip is " + target)
print("your time now is " + str(datetime.now()))

try:
    for port in range(50,85):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(2)
        result = soc.connect_ex((target, port))
        
        if result == 0:
            print(f"the port {port} is open ")
            
        soc.close()

except KeyboardInterrupt:
    print("\nyou stop the programme ")
    sys.exit()

except socket.gaierror:
    print("Hostname is not defined")
    sys.exit()

except socket.error:
    print("A server error occurred")
    sys.exit()
