import os
import subprocess
import shutil
import webbrowser

parent_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/../")
app_name = os.path.basename(parent_dir)

# Remove existing files
app_dir = os.path.join(parent_dir, "app")
for filename in os.listdir(app_dir):
    filepath = os.path.join(app_dir, filename)
    if os.path.isdir(filepath):
        shutil.rmtree(filepath)
    else:
        os.remove(filepath)

# Install framework in temporary folder
command = "docker exec -it {app_name}_php_1 composer create-project symfony/website-skeleton /var/www/app"
command = command.format(app_name=app_name)

subprocess.call(command, shell=True)

# Starting in browser
webbrowser.open("http://localhost", new=1, autoraise=True)