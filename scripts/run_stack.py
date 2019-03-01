import sys
import os
import subprocess

parent_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/../")

# Base config
compose_config = "-f {docker_compose_file}".format(docker_compose_file=parent_dir + "/docker-compose.yml")

# Extra config files
files = {
    "rabbit": parent_dir + "/docker-compose.mq.yml",
    "msql": parent_dir + "/docker-compose.mssql.yml"
}

for fileKey in sys.argv[1:]:
    if fileKey in files.keys():
        compose_config += " -f {extra_compose_file}".format(extra_compose_file=files.get(fileKey))

# Run the UP command
command = "python {ip_update_script} && docker-compose {compose_config} up -d".format(
    ip_update_script=parent_dir + "/scripts/update_www_conf.py",
    compose_config=compose_config
)

subprocess.call(command, shell=True)
