import os
import subprocess

app_root_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/../").split("/")[-1]
app_dir_name = app_root_path.split(b"/")[-1]

command = "docker exec -it {app_name}_php_1 /bin/bash --init-file /root/.bash_profile"
command = command.format(app_name=app_dir_name)

subprocess.call(command, shell=True)
