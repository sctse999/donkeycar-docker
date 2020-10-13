export HOST_IP=$(ip addr show docker0 | grep -Po 'inet \K[\d.]+')

echo $HOST_IP

docker-compose -f docker-compose.yml up -d --build 