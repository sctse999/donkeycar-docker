FROM python:3.7-buster
# FROM alpine:3

ARG venv_name=env

RUN apt-get clean
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install git
RUN apt-get -y install vim net-tools


RUN apt-get -y install build-essential python3 python3-dev python3-pip python3-virtualenv python3-numpy python3-pandas i2c-tools avahi-utils joystick libopenjp2-7-dev libtiff5-dev gfortran libatlas-base-dev libopenblas-dev libhdf5-serial-dev git ntp
RUN python3 -m venv env --system-site-packages

RUN git clone https://github.com/robocarstore/donkeycar
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN . /$venv_name/bin/activate && pip install -r requirements.txt
# RUN apt-get install build-essential python3 python3-dev python3-pip python3-virtualenv python3-numpy python3-picamera python3-pandas python3-rpi.gpio i2c-tools avahi-utils joystick libopenjp2-7-dev libtiff5-dev gfortran libatlas-base-dev libopenblas-dev libhdf5-serial-dev git ntp

WORKDIR /donkeycar

RUN git checkout robocarstore_v4
#RUN git checkout v4_dev # For dev only
RUN git pull
RUN . /$venv_name/bin/activate && pip install -e .

# Install KERAS VIS and ffmpeg for video generation
RUN . /$venv_name/bin/activate && pip install git+https://github.com/autorope/keras-vis.git

RUN apt-get -y install ffmpeg

RUN . /$venv_name/bin/activate && donkey createcar --path ~/mycar --overwrite

WORKDIR /
RUN git clone https://github.com/tawnkramer/gym-donkeycar

WORKDIR /gym-donkeycar
RUN . /$venv_name/bin/activate && pip install -e .[gym-donkeycar]

WORKDIR /
RUN git clone https://github.com/robocarstore/donkeycar-console

WORKDIR /donkeycar-console
RUN . /$venv_name/bin/activate && pip install -r requirements/production.txt

# Run the donkeycar console service
RUN . /$venv_name/bin/activate && python manage.py migrate

# Activate the virtual env upon bash start
WORKDIR /root/mycar
RUN echo "source /env/bin/activate" > /root/.bashrc

# Run the donkeycar console service
ENV RUNTIME_ENV=${venv_name}

CMD /${RUNTIME_ENV}/bin/python /donkeycar-console/manage.py runserver 0.0.0.0:8000
