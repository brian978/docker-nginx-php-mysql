# Basic services
* Nginx: 1.15
* PHP-FPM: 7.2
* MySQL: 5.7
* memcached: 1.5

# Extra services
* Microsoft SQL Server: 2017 (latest)
* RabbitMq: 3.7

# Before starting
Before you start using this setup you need to make a copy for www.conf.dist (in  container-config/fpm) and create a file
called www.conf (which is excluded from the repo)

# To connect to a docker container you just need to run
`python scripts/run_stack.py`

## Connecting the PHP container with a provisioned bash
`python scripts/tty_php.py`

# Flexible setup
The base configuration only includes Nginx, PHP MySQL and Memcached. If you want the other services you must pass the
following parameters as follows:
* rabbit - if you want RabbitMq
* msql - if you want MySQL server

The full command would look like this
`python scripts/run_stack.py rabbit msql`
