MODEL_NAME=job_4.h5
SPAWN_INTERVAL_IN_SEC=2
NO_OF_NPC=3

# for i in {1..$NO_OF_NPC}
for (( i=2; i<=$NO_OF_NPC; i++ ))
do
    echo "Start #$i car"
    sleep $SPAWN_INTERVAL_IN_SEC

    docker exec donkeycar$i /env/bin/python manage.py drive --model models/$MODEL_NAME &
    # docker exec -it donkeycar2 /env/bin/python manage.py drive --model models/$MODEL_NAME &
done


