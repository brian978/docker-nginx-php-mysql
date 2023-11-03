#!/bin/bash

# Get parent directory
parent_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"

# Ensure we have the required configuration files for the docker services
# FPM
fpm_file="${parent_dir}/services/fpm/www.conf"
[[ ! -f $fpm_file ]] && cp "${fpm_file}.dist" "$fpm_file"

# Xdebug
xdebug_file="${parent_dir}/services/php/conf.d/xdebug.ini"
[[ ! -f $xdebug_file ]] && cp "${xdebug_file}.dist" "$xdebug_file"

# Nginx
nginx_file="${parent_dir}/services/nginx/conf.d/default.conf"
[[ ! -f $nginx_file ]] && cp "${nginx_file}.dist" "$nginx_file"

# Base config
compose_config="-f ${parent_dir}/docker-compose.yml"

# Extra config files
for fileKey in "$@"; do
    case "$fileKey" in
        rabbit)
            compose_config+=" -f ${parent_dir}/docker-compose.mq.yml"
            ;;
        msql)
            compose_config+=" -f ${parent_dir}/docker-compose.mssql.yml"
            ;;
        *)
            echo "Unknown option: $fileKey"
            ;;
    esac
done

# Run the UP command
ip_update_script="${parent_dir}/scripts/provision_xdebug.sh"
command="sh $ip_update_script && docker-compose $compose_config up -d"
echo "$command"
eval "$command"
