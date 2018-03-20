# To connect to a docker container you just need to run
docker exec -it {{ container_name }} /bin/bash

For example for the default instalation of the environment, the {{ container_name }} will be _nginxphpmysql_php_1_

## Connecting the PHP container with a provisioned bash
All you need to do is run the tty_php.sh bash script with the {{ conainer_name }} like so (just remember to use to proper name):
`scripts/tty_php.sh nginxphpmysql_php_1`


# Connecting from a container to another container
Since the containers are basically in their own private network you will need to use the internal port of the target container and the {{ container_name }}

For example if you want to connect from the PHP container to the MySQL container all you need to do is use _nginxphpmysql_db_1_ as the {{ container_name }} and 3306 as the port (not the port that is forwarded outside the network, 33061)
