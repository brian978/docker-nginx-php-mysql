#!/bin/bash

container=$1

if [ "$container" != "" ]
then
    docker exec -it $container /bin/bash --init-file /root/.bash_profile
else
    printf "Please provide a container name as the script argument\n\n"
fi
