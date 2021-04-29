# This script will delete all cars database, removing all training record
# It will not delete existing data tub and models

import subprocess

for i in range(1,10):
    try:
        command = f"docker volume rm mycar{i}_db"
        print(subprocess.check_output(command, shell=True).decode("utf-8"))
    except Exception as e:
        print(e)
