#!/usr/bin/python3

import sys, re

"""The script will take file as an input parameter """
f = open(sys.argv[1],'r')
# Enter the ip address you are searching for in the file
ip = input("IP: ")
# Reads the given parameter file
text = f.read()
# create empty list
ips = []
# regex to find pattern mattching to ip addresses
regex = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',text)

# check if the regex is not none will never be
if regex is not None:
    # looking for the match in the regex
    for match in regex:
        # if match is found in the list append it
        if match not in ips:
            ips.append(match)
            # Search the ip in the ip list from the file and display
            if ip in match:
                print(f"{ip} is in the file")
                break
        else:
            print(f"{ip} not found")
            break


"""
#============================= Sample Script Output ===========================#

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
