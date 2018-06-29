import sys
import os
import subprocess

parent_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/../")

command = "python {ip_update_script} && docker-compose -f {docker_compose_file} up -d"
command = command.format(
                         ip_update_script = parent_dir + "/scripts/update_www_conf.py",
                         docker_compose_file = parent_dir + "/docker-compose.yml"
                        )


subprocess.call(command, shell=True)
