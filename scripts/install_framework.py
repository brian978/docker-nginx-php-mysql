import os
import subprocess

app_root_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/../").split("/")[-1]
app_dir_name = app_root_path.split(b"/")[-1]

install_cmd = "create-project --prefer-dist laravel/laravel /var/www/app/laravel"
cleanup_script = "/usr/local/scripts/install_cleanup.sh"

# Install laravel in temporary folder
command = "docker exec -it {app_name}_php_1 php /usr/local/bin/external/composer.phar {composer_cmd}"
command = command.format(app_name=app_dir_name, composer_cmd=install_cmd)

subprocess.call(command, shell=True)

# Run the cleanup process
command = "docker exec -it {app_name}_php_1 /bin/bash --init-file /root/.bash_profile {cleanup_script}"
command = command.format(app_name=app_dir_name, cleanup_script=cleanup_script)

subprocess.call(command, shell=True)
