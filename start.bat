docker-compose -f docker-compose-win-mac.yml up -d

docker exec donkeycar sh -c "/env/bin/donkey createcar --path /root/mycar --overwrite"
