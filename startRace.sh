ls -alh models/current/*.h5

read -p "Is everything good? " -n 1 -r
echo    # (optional) move to a new line

COUNTER=1

for model in models/current/*.h5; do
    # echo $filename        \
    fullname=$(basename -- "$model")
    extension="${fullname##*.}"
    filename="${fullname%.*}"

    echo "Copying $fullname to car $COUNTER"

    cp $model mycar$COUNTER/models/

    echo "GYM_CONF[\"car_name\"] = \"$filename\"" >> mycar$COUNTER/myconfig.py

    docker exec donkeycar$COUNTER /env/bin/python manage.py drive --model models/$fullname &

    COUNTER=$((COUNTER+1))
    
done


# if [[ $REPLY =~ ^[Yy]$ ]]
# then
#     echo "you type Y"
#     docker exec donkeycar$COUNTER /env/bin/python manage.py drive --model models/m1.h5 &
#     docker exec donkeycar$COUNTER /env/bin/python manage.py drive --model models/m2.h5 &
# else
#     echo "Quitted"
# fi

