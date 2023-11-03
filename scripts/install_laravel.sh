#!/bin/bash

# Function to run a command in the php container
run_in_php_container() {
    docker compose run --rm php /bin/bash -c "$1"
}

run_in_php_container "rm .gitkeep  && composer create-project laravel/laravel ."

echo "Laravel installation completed."
