#!/bin/bash

# Get parent directory
parent_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")"/.. && pwd)"

# File paths
config_file="${parent_dir}/services/php/conf.d/xdebug.ini"

# IP detect based on OS
case "$(uname -s)" in
    Darwin)
        ip=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
        ;;
    Linux)
        ip=$(ip route get 8.8.8.8 | head -n1 | awk '{print $7}')
        ;;
    CYGWIN*|MINGW32*|MSYS*)
        ip=$(ipconfig | grep -i "ipv4" | head -n1 | awk '{print $NF}')
        ;;
    *)
        echo "Unknown OS"
        exit 1
        ;;
esac

# Update the Xdebug config
while IFS= read -r line; do
    if [[ $line == *"xdebug.client_host"* ]]; then
        echo "xdebug.client_host=${ip}"
    else
        echo "$line"
    fi
done < "$config_file" > "${config_file}.tmp"
mv "${config_file}.tmp" "$config_file"
