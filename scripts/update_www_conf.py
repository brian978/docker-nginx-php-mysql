import sys
import os
import socket
import fileinput

parent_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/../")

# IP detect
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_obj.connect(("8.8.8.8", 80))
ip = socket_obj.getsockname()[0]

# Update the PHP-FPM file
for line in fileinput.input(parent_dir + "/container-config/fpm/www.conf", inplace=True):
    if line.find("php_admin_value[xdebug.remote_host]") != -1:
        print("php_admin_value[xdebug.remote_host] = " + ip)
    else:
        sys.stdout.write(line)

# Update the Docker compose file
for line in fileinput.input(parent_dir + "/docker-compose.yml", inplace=True):
    if line.find("ADV_HOST") != -1:
        print("      ADV_HOST: " + ip)
    else:
        sys.stdout.write(line)
