import sys
import os
import subprocess

app_root_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/../").split("/")[-1]
app_dir_name = app_root_path.split("/")[-1]

# Install laravel in temporary folder
command = "docker exec -it {app_name}_php_1 php /usr/local/bin/external/composer.phar create-project --prefer-dist laravel/laravel /var/www/app/laravel"
command = command.format(app_name = app_dir_name)

subprocess.call(command, shell=True)

# Run the cleanup process
command = "docker exec -it {app_name}_php_1 /bin/bash --init-file /root/.bash_profile /usr/local/scripts/laravel_cleanup.sh"
command = command.format(app_name = app_dir_name)

subprocess.call(command, shell=True)
