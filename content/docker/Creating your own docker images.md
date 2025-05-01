---
title: Docker images
tags:
  - ethernetdude
  - Docker
---
in case, if you are developing an application & decide to run it as container or if you want to install something as a container that is not available on docker hub, then you would have to create your own docker image.

**How to create your image ?**

First, create a file named "dockerfile" & write down the instructions such as where to copy the source code from, what is the entry point & where to install the application etc..

Here I am going to create a sample dockerfile 

On the left hand side commands are instructions, Things like FROM, RUN, COPY & ENTRYPOINT are instructions & the inputs on the right are instructions.


```
FROM Ubuntu 

%% All docker files start from a from instruction. They need a base image %%

RUN apt-get update && apt-get -y install python 

%% This will install dependencies basically instructs docker to run a particular command on the base image. %%

RUN pip install flask flask-mysql

COPY . /opt/source-code

%% This copies the source code to the docker image. %%

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run 

%% This entrypoint allows us to specify a command that will be run when we run the image as container. %%``

%% use the docker build command to create a docker image. -t species the tag name for image%%
docker build . -f dockerfile -t kkapil/my-custom-app

%% Use the docker push command to keep the image in docker hub %%

docker push kkapil/my-custom-app
```

**Note**: You have to login first to docker hub using the `docker login` command to be able to push the image.

Docker images are created in a Layered fashion. Each layer is built on top of the previous layer and is cached, so if you get an error in step 3, when you reattempt, step1 & step2 such as building the base os are already cached and process starts from step 3.

**Environment Variables:** Environment variables are something that can change every time an instance of container running the application is created. While the environment variable itself is written into the application code. We can set them at the time of running the docker container by using the "-e" option with the docker run command.

```
docker run -e {environment-variable}={value} {docker-image-name}
```

We can find the environment variable on a container already running by using the docker inspect command.

**Command & Entry points:** 

As you are probably aware by now that a container only lives as long as the process inside it keeps running. 

When the container initially starts, It has to run a process, the CMD is used in the docker file to specify this.

We can override the command run at the startup of container 

```
docker run {image-name } {command}
```

Now, if you want to make this change permanent, then you should use the base image and create your own image with the CMD specified in the docker file.

**Entry Point :** The entry point instruction is like a command instruction to specify the program that you want to run at the start & whatever you have specified in the CMD will get appended to the entry point.

For example, in a docker file if you have the entry point as sleep & the cmd as 5, then the command that would be run at startup of container is sleep 5.

