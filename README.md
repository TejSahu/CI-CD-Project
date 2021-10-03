
Create a simple Python / flask application (e.g Single endpoint in Flask which will return some value with a test case).

# Simple flask app to print best NFS games in JSON format

from flask import Flask, jsonify


app = Flask(__name__)

# Best Need for Speed Games
games = [{'id': 0,
          'title': 'Need for Speed Heat',
          'year_published': '2019'},
         {'id': 1,
          'title': 'Need for Speed Most Wanted',
          'published': '2005'},
         {'id': 2,
          'title': 'Need for Speed Underground 2',
          'published': '2004'}]


@app.route('/')
def home():
    return '''<h1>Best Need for Speed titles</h1>
<p>API Sample returning best NFS Games</p>'''


@app.route('/games')
def api_all():
    return jsonify(results=games)


app.run()

Dockerize the above application and push it to the docker hub or any registry.

## Docker set up

sudo yum install docker

# needs to be done if service is stopped
sudo service docker start

## Building an image of above code
# set base image (host OS)
FROM python:3.7

# copy the dependencies file to the working directory
ADD . /app

# set the working directory
WORKDIR /app

# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
CMD ["python", "api.py"]

# Build an image with Dockerfile
docker build -t sampleapi:latest .

# to run a docker with psudeo tty to test the working build
docker run -it -p 5000:5000 sampleapi

# need to login to docker before pushing
docker login -u username and then password

# docker tag and push
docker tag imageid zingalatej/exercise:firstone
docker push firstone

Create one ec2 instance using terraform script



Setup Jenkins job which will build a new docker image when you push some changes to the branch and will deploy the updated code on EC2

## Setting up Jenkins

sudo yum install jenkins

sudo systemctl start jenkins

sudo systemctl status jenkins


## Setting up ansible on remote machine

python3 -m pip install ansible

ansible-galaxy collection install community.docker

ansible-playbook pulldocker.yml  --syntax-check
