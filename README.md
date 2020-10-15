# Donkeycar Docker Images
This docker image allows you to run [donkey car](http://donkeycar.com/) without installing it. The primary use case would be running this docker image on your PC (not Pi or Jetson nano) and use it together with the simulator. You can then use the mobile app to control the car in the simulator and perform training and test autopilot within the app.

## Features
- Pre-configured docker image with the Donkey Car and other dependencies
- Contains pre-configured Donkeycar-console[](https://github.com/robocarstore/donkeycar-console) to work with mobile app
- Support [donkey car mobile app](https://medium.com/robocar-store/robocar-controller-quick-start-guide-bdf8cb16d7ce)


### Windows Requirement
- Min. Windows 10 Home, version 1903 or higher
- Docker Desktop 2.3.0.5

## How to run

### Linux
```
git clone https://github.com/sctse999/donkeycar-docker
cd donkeycar-docker
./start.sh
./stop.sh
```

### Windows
```
git clone https://github.com/sctse999/donkeycar-docker
cd donkeycar-docker
./start.bat
./stop.bat
```

## Running it with the simulator and mobile app

1. Download and run the [Donkey Car Simualtor](https://github.com/tawnkramer/gym-donkeycar/releases)

2. Run this docker image

3. Install the mobile app and follow the medium article to use the mobile app

