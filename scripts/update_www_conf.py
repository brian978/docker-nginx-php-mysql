import sys
import os
import socket
import fileinput


def get_ip_address():
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_obj.connect(("8.8.8.8", 80))

    return socket_obj.getsockname()[0]


ip = get_ip_address()
file = os.path.abspath("../container-config/fpm/www.conf")

for line in fileinput.input(file, inplace=True):
    if line.find("php_admin_value[xdebug.remote_host]") != -1:
        print("php_admin_value[xdebug.remote_host] = " + ip)
    else:
        sys.stdout.write(line)
