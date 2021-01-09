import os
import subprocess

parent_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/../")

command = "docker exec -it {app_name}_php_1 bash"
command = command.format(app_name=os.path.basename(parent_dir))

subprocess.call(command, shell=True)
