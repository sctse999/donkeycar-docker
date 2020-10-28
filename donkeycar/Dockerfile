FROM python:3.7-buster
# FROM alpine:3

ARG venv_name=env
ARG venv_path=/env
# ARG dc_venv_path=/env_dc

RUN apt-get clean
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install git
RUN apt-get -y install vim net-tools


RUN apt-get -y install build-essential python3 python3-dev python3-pip python3-virtualenv python3-numpy python3-pandas i2c-tools avahi-utils joystick libopenjp2-7-dev libtiff5-dev gfortran libatlas-base-dev libopenblas-dev libhdf5-serial-dev git ntp
RUN python3 -m venv env --system-site-packages

RUN git clone https://github.com/sctse999/donkeycar

# RUN apt-get install build-essential python3 python3-dev python3-pip python3-virtualenv python3-numpy python3-picamera python3-pandas python3-rpi.gpio i2c-tools avahi-utils joystick libopenjp2-7-dev libtiff5-dev gfortran libatlas-base-dev libopenblas-dev libhdf5-serial-dev git ntp

WORKDIR /donkeycar

RUN git checkout master
RUN . /$venv_name/bin/activate && pip install -e .
RUN . /$venv_name/bin/activate && pip install tensorflow==1.13.1

# Install KERAS VIS and ffmpeg for video generation
RUN . /$venv_name/bin/activate && pip install git+https://github.com/autorope/keras-vis.git
RUN . /$venv_name/bin/activate && pip install opencv-python
RUN apt-get -y install ffmpeg

RUN . /$venv_name/bin/activate && donkey createcar --path ~/mycar --overwrite

WORKDIR /
RUN git clone https://github.com/tawnkramer/gym-donkeycar

WORKDIR /gym-donkeycar
RUN . /$venv_name/bin/activate && pip install -e .[gym-donkeycar]

WORKDIR /
RUN python3 -m venv $venv_path --system-site-packages
RUN git clone https://github.com/sctse999/donkeycar-console

WORKDIR /donkeycar-console
RUN . $venv_path/bin/activate && pip install -r requirements/production.txt

# Run the donkeycar console service
ENV RUNTIME_ENV=${venv_path}

CMD ${RUNTIME_ENV}/bin/python manage.py runserver 0.0.0.0:8000

# CMD ${RUNTIME_ENV}/bin/gunicorn dkconsole.wsgi -b 0.0.0.0:8000 -c gunicorn.config.py

# CMD npm run start:${RUNTIME_ENV}

# RUN 

# First copy only setup.py, run pip install, and then copy the whole donkey dir.
# This is so only changes to setup.py trigger a pip install.
# COPY ./setup.py /donkey/setup.py
# RUN pip install -e /donkey/[server]
# COPY . /donkey/

# # Change workdir and run scripts/setup.py

# RUN python /donkey/scripts/setup.py

# EXPOSE 8886
# EXPOSE 8887

# Run the server
# ENTRYPOINT ["python", "/donkeycar/scripts/serve.py"]
