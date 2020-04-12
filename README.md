# Basic services
* Nginx: 1.17
* PHP-FPM: 7.4
* MySQL: 5.7
* memcached: 1.6

# Extra services
* Microsoft SQL Server: 2017 (latest)
* RabbitMq: 3.7

# To start up the stack you need to run
`python scripts/run_stack.py`

## Connecting the PHP container with a provisioned bash
`python scripts/tty_php.py`

# Flexible setup
The base configuration only includes Nginx, PHP, MySQL and Memcached. If you want the other services you must pass one of
the following parameters as follows:
* rabbit - if you want RabbitMq
* msql - if you want MySQL server

Examples:
1. Adding RabbitMq support: `python scripts/run_stack.py rabbit`
2. Adding Microsoft SQL Server support: `python scripts/run_stack.py msql`
3. Adding support for both: `python scripts/run_stack.py rabbit msql`

