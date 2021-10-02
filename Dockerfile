# set base image (host OS)
FROM python:3.7

# copy the dependencies file to the working directory
COPY . /app

# set the working directory
WORKDIR /app
# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
CMD python api.py

