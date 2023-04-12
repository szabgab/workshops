# Getting started with Docker

[Docker](https://www.docker.com/) is the de-facto standard in containerization.
It allows you to create an environment that can easily be used for development, testing, and deployment
minimizing the chances of problems that stem from the gap between these environments.

It also provides a much smoother path to onboard new engineers (developers, testers, anyone) as they don't have to spend ages understanding and
setting up their development environment.


## Content

We'll start from the beginning and we'll see how far we can get in this material.

Remember, this is a workshop with hands-on experience. I'll explain some stuff and then you get exercises to do.


* Install Docker
* docker run hello-world
* Docker image vs container
* Docker Registry / Docker HUB
* Docker Daemon, Client
* Create simple image
* Distribute a command line tool
* Distribute a web application (just flask)
* Distribute a web application flask + nginx
* Distribute a web application flask + nginx + MongoDB
* Create an image with all the dependencies of a build and then reuse that image in every later stage. Rebuild the base image whenever the requirements file was changed.
* docker pull
* Run several Docker images at once
* Create an image in the repository (from github)
* Run multi-host applications using `docker-compose`.
* Linux, OSX, and Windows
* What are the layers?

## Prerequisite:

* You need to bring your computer where you can install things.
* You can go ahead, download and install Docker.
* [Docker Desktop for Windows](https://docs.docker.com/docker-for-windows/install/)
* [Docker for Mac](https://docs.docker.com/docker-for-mac/install/)
* Linux: `sudo apt-get install docker` or `yum install docker`

