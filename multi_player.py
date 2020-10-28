import os
import subprocess

command = "docker ps"
CONSOLE_BASE_PORT = 8000                # 8001, 8002, 8003
WEB_CONTROLLER_BASE_PORT = 10887        # 11887, 12887, 13887
IMAGE_NAME = "robocarstore/donkeycar:latest"

no_of_racers = int(input("Enter number of racer: "))

# Clean mycar 
subprocess.check_output("rm -rf mycar/data/*", shell=True)
subprocess.check_output("rm -rf mycar/models/*", shell=True)
subprocess.check_output("rm -rf mycar/movies/*", shell=True)


if 0 < no_of_racers <= 10:
    for i in range(1, no_of_racers+1):
        subprocess.check_output(f"rm -rf mycar{i}", shell=True)
        subprocess.check_output(f"mkdir mycar{i}", shell=True)


        console_port = CONSOLE_BASE_PORT + i
        web_controller_port = WEB_CONTROLLER_BASE_PORT + i * 1000

        command = ["docker run"]
        command.append(f"-p {console_port}:8000")
        command.append(f"-p {web_controller_port}:8887")
        command.append("-v mycar:/root/mycar")
        command.append("-v donkeycar-console:/donkeycar-console")
        command.append(f"-e WEB_CONTROL_PORT={web_controller_port}")
        command.append(f"-e mode=docker")
        command.append(f"--name donkeycar{i}")
        command.append(f"-d {IMAGE_NAME}")

        print(" ".join(command))
        print(subprocess.check_output(" ".join(command), shell=True))

        command = f"docker exec donkeycar{i} sh -c '/env/bin/donkey createcar --path /root/mycar --overwrite'"
        print(subprocess.check_output(command, shell=True))




