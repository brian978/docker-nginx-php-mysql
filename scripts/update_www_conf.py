import sys
import os
import socket
import fileinput
from shutil import copyfile

parent_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/../")

# File paths
config_file = os.path.join(parent_dir, "services", "fpm", "www.conf")

# IP detect
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_obj.connect(("8.8.8.8", 80))
ip = socket_obj.getsockname()[0]

# Update the PHP-FPM file
for line in fileinput.input(config_file, inplace=True):
    if line.find("php_admin_value[xdebug.remote_host]") != -1:
        print("php_admin_value[xdebug.remote_host] = " + ip)
    else:
        sys.stdout.write(line)
