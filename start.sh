#!/bin/bash

system="$(uname -s)"
case "${system}" in
    Linux*)     
        export HOST_IP=$(ip addr show docker0 | grep -Po 'inet \K[\d.]+')
        echo $HOST_IP
        docker-compose -f docker-compose-linux.yml up -d --build 
        ;;
    Darwin*)
        docker-compose -f docker-compose-win-mac.yml up -d --build 
        ;;
    *)          
        echo "OS Not supported"
        ;;
esac
