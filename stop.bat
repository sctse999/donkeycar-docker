docker-compose -f docker-compose-win-mac.yml down

docker rm $(docker stop $(docker ps -a -q --filter ancestor=robocarstore/donkeycar --format="{{.ID}}"))

REM FOR /f "tokens=*" %%i IN ('docker ps -a -q') DO docker rm -f %%i
