#!/bin/bash

system="$(uname -s)"
case "${system}" in
    Linux*)     
        export HOST_IP=$(ip addr show docker0 | grep -Po 'inet \K[\d.]+')
        echo $HOST_IP
        docker-compose -f docker-compose-linux.yml down
        ;;

    Darwin*)
        docker-compose -f docker-compose-win-mac.yml down
        ;;
    *)
        echo "OS Not supported"
        ;;
esac

# docker rm $(docker stop $(docker ps -a -q --filter ancestor=robocarstore/donkeycar --format="{{.ID}}"))
docker rm $(docker stop $(docker ps -a -q --filter name=donkeycar --format="{{.ID}}"))
