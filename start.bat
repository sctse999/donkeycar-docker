docker-compose -f docker-compose-win-mac.yml up -d --build

docker exec donkeycar2 sh -c "/env/bin/donkey createcar --path /root/mycar --overwrite"
