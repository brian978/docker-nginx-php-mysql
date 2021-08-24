import sys
import os
import subprocess

parent_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/../")
arguments = "bash" if len(sys.argv) == 1 else " ".join(sys.argv[1:])

command = "docker exec -it {app_name}_php_1 {args}"
command = command.format(app_name=os.path.basename(parent_dir), args=arguments)

subprocess.call(command, shell=True)
