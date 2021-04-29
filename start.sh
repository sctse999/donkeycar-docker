#!/bin/bash

system="$(uname -s)"
docker pull robocarstore/donkeycar:latest
case "${system}" in
    Linux*)     
        export HOST_IP=$(ip addr show docker0 | grep -Po 'inet \K[\d.]+')
        echo $HOST_IP
        
        docker-compose -f docker-compose-linux.yml up -d
        # docker-compose -f docker-compose-linux-dev.yml up -d --build
        ;;
    Darwin*)
        docker-compose -f docker-compose-win-mac.yml up -d --build 
        ;;
    *)          
        echo "OS Not supported"
        ;;
esac

# Reinstall donkey car if binding a local volume for development
docker exec donkeycar /bin/bash -c  "source /env/bin/activate && cd /donkeycar && pip install -e .[pc]"

docker exec donkeycar sh -c '/env/bin/donkey createcar --path /root/mycar --overwrite'
docker exec donkeycar sh -c 'find /root/mycar -type f -exec chmod 666 {} \;'
docker exec donkeycar sh -c 'find /root/mycar -type d -exec chmod 777 {} \;'

