docker-compose -f docker-compose-win-mac.yml down


docker rm $(docker stop $(docker ps -a -q --filter ancestor=robocarstore/donkeycar --format="{{.ID}}"))