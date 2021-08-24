import sys
import os
import socket
import fileinput

parent_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/../")

# File paths
config_file = os.path.join(parent_dir, "services", "php", "conf.d", "xdebug.ini")

# IP detect
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_obj.connect(("8.8.8.8", 80))
ip = socket_obj.getsockname()[0]

# Update the Xdebug config
for line in fileinput.input(config_file, inplace=True):
    if line.find("xdebug.client_host") != -1:
        print("xdebug.client_host=" + ip)
    else:
        sys.stdout.write(line)
