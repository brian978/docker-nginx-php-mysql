# Basic services
* Nginx: latest
* PHP-FPM: 8.2
* MariaDB: latest
* memcached: latest

# Extra services
* Microsoft SQL Server: 2017 (latest)
* RabbitMq: latest

# To start up the stack you need to run
`make start`

## Connecting the PHP container with a provisioned bash
`make cli`

## Installing Laravel
`make install`

# Flexible setup
The base configuration only includes Nginx, PHP, MySQL and Memcached. If you want the other services you must pass one
of the following parameters as follows:
* rabbit - if you want RabbitMq
* msql - if you want MySQL server

Examples:
1. Adding RabbitMq support: `sh scripts/run.sh rabbit`
2. Adding Microsoft SQL Server support: `sh scripts/run.sh msql`
3. Adding support for both: `sh scripts/run.sh rabbit msql`

