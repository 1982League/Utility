#!/usr/bin/python3

import sys, re

f = open(sys.argv[1],'r')
ip = input("IP: ")
text = f.read()
ips = []
regex = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',text)
if regex is not None:
    for match in regex:
        if match not in ips:
            ips.append(match)
            if ip in match:
                print(f"{ip} is in the file")
                break
        else:
            print(f"{ip} not found")
            break

#============================= Sample Script Output ===========================#
"""
./find_ip1.py ip.txt
IP: 10.1.81.1
10.1.81.1 is in the file
#==============================================================================#

#============================= Sample Script Output ===========================#

./find_ip1.py ip.txt
IP: 10.0.8.1
10.0.8.1 not found
[sjoshi@se1-admin-baleroc01 myscripts]$
#==============================================================================#
"""
