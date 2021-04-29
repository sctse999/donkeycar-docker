import os
import subprocess
from pathlib import Path
from sys import platform


command = "docker ps"
CONSOLE_BASE_PORT = 8000               # 8000, 8001, 8002, 8003
WEB_CONTROLLER_BASE_PORT = 8887        # 8887, 9887, 10887
IMAGE_NAME = "robocarstore/donkeycar:latest"

no_of_racers = int(input("Enter number of racer: "))

# Clean mycar 
# subprocess.check_output("rm -rf mycar/data/*", shell=True)
# subprocess.check_output("rm -rf mycar/models/*", shell=True)
# subprocess.check_output("rm -rf mycar/movies/*", shell=True)


if 0 < no_of_racers <= 10:
    subprocess.check_output(f"docker pull {IMAGE_NAME}", shell=True)

    if platform == "linux" or platform == "linux2":
        command = "ip addr show docker0 | grep -Po 'inet \K[\d.]+'"
        host_ip = subprocess.check_output(command, shell=True).strip().decode("utf-8") 
    

    for i in range(1, no_of_racers+1):
        carapp_path = Path.cwd() / f"mycar{i}"
        console_path = Path.cwd() / "donkeycar-console"

        try:
            os.mkdir(carapp_path)
        except:
            pass

        console_port = CONSOLE_BASE_PORT + i - 1
        web_controller_port = WEB_CONTROLLER_BASE_PORT + (i-1) * 1000
        db_volume_name = f"mycar{i}_db"
        
        command = ["docker run"]
        command.append(f"-p {console_port}:8000")
        command.append(f"-p {web_controller_port}:{web_controller_port}")
        command.append(f"-v {carapp_path}:/root/mycar")
        command.append(f"-v {db_volume_name}:/donkeycar-console")
        command.append(f"-e WEB_CONTROL_PORT={web_controller_port}")
        command.append(f"-e mode=docker")
        command.append(f"--name donkeycar{i}")
        command.append(f"--hostname donkeycar{i}")

        if platform == "linux" or platform == "linux2":
            command.append(f"--add-host host.docker.internal:{host_ip}")
        command.append(f"-d {IMAGE_NAME}")

        print(" ".join(command))
        print(subprocess.check_output(" ".join(command), shell=True).decode("utf-8"))

        command = f"docker exec donkeycar{i} sh -c \"/env/bin/donkey createcar --path /root/mycar --overwrite\""
        print(subprocess.check_output(command, shell=True).decode("utf-8"))

        command = f"docker cp mycar/myconfig.py donkeycar{i}:/root/mycar/myconfig.py"
        print(subprocess.check_output(command, shell=True).decode("utf-8"))

        command = f"docker cp mycar/setup.json donkeycar{i}:/root/mycar/setup.json"
        print(subprocess.check_output(command, shell=True).decode("utf-8"))

        # python search racer name and rename racename to racer1, racer2, racer3
        file_object = open(f'mycar{i}/myconfig.py', 'a')

        # Append 'hello' at the end of file
        file_object.write(f'\nGYM_CONF["car_name"] = "Racer {i}"\n')
        
        # Close the file
        file_object.close()




