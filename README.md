# Donkeycar Docker Images
This docker image allows you to run [donkey car](http://donkeycar.com/) without installing it. The primary use case would be running this docker image on your PC (not Pi or Jetson nano) and use it together with the simulator. You can then use the mobile app to control the car in the simulator and perform training and test autopilot within the app.

## Features
- Pre-configured docker image with the Donkey Car and other dependencies
- Contains pre-configured Donkeycar-console[](https://github.com/robocarstore/donkeycar-console) to work with mobile app
- Support [donkey car mobile app](https://medium.com/robocar-store/robocar-controller-quick-start-guide-bdf8cb16d7ce)

### Version
- Donkey Car master branch (Currently v3.1.5)

### Windows Requirement
- Min. Windows 10 Home, version 1903 or higher
- Docker Desktop 2.3.0.5

## How to run

### Linux
Install docker. Follow instruction [here](https://linuxhint.com/install_configure_docker_ubuntu/) or [here](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04).

Then, do the following:
```
git clone https://github.com/sctse999/donkeycar-docker
cd donkeycar-docker
./start.sh
./stop.sh
```

### Windows
Install docker. Follow instruction [here](https://docs.docker.com/docker-for-windows/install-windows-home/).

```
git clone https://github.com/sctse999/donkeycar-docker
cd donkeycar-docker
./start.bat
./stop.bat
```

## Running it with the simulator and mobile app

1. Download and run the [Donkey Car Simualtor](https://github.com/tawnkramer/gym-donkeycar/releases)

2. Run this docker image

3. Install the mobile app and follow this [medium article](https://medium.com/robocar-store/robocar-controller-quick-start-guide-bdf8cb16d7ce) to use the mobile app

## Multiple docker in same host
```
python multi_player.py
```


## Change log

### 20201028:
- Support multiple player in same host
- Both donkey and donkeycar-console share the same virtual environment now
- donkeycar-console will honor the WEB_CONTROL_PORT setting from myconfig.py 
- Clean mycar folder
- Windows compatibility for multi_player.py