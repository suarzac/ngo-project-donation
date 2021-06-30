# importing base image
FROM python:3.9

# updating docker host or host machine
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# changing current working directory to /usr/src/app
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copying requirement.txt file to present working directory
COPY requirements.txt ./

# installing dependency in container
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copying all the files to present working directory
COPY . /usr/src/app

# informing Docker that the container listens on the
# specified network ports at runtime i.e 8000.
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]