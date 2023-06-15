FROM ubuntu:latest

# libraries
RUN apt-get update
RUN apt-get -y install python3 python3-pip

# create user
RUN groupadd -r ctf && useradd -r -g ctf ctf

# challenge resources
# COPY files/ /home/ctf/files/
# COPY templates/ /home/ctf/templates/
# COPY flag.txt /home/ctf/flag.txt
# COPY requirements.txt /home/ctf/requirements.txt
# COPY app.py /home/ctf/app.py

COPY . /home/ctf

# permissions
RUN chown -R root:ctf /home/ctf
RUN chmod 550 /home/ctf/app.py
RUN chmod 440 /home/ctf/flag.txt
RUN chmod 440 /home/ctf/requirements.txt
RUN chmod 440 /home/ctf/templates/*
RUN chmod 440 /home/ctf/files/*

# install requirements
RUN python3 -m pip install -r /home/ctf/requirements.txt

# switch to ctf user
USER ctf



# run app.py
CMD ["python3", "/home/ctf/app.py"]