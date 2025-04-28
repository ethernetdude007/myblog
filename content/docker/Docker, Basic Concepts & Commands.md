---
title: Basic Docker Concepts & Commands.
tags:
  - Docker
  - ethernetdude
---
**docker run :** The docker run command is used to create a container from an image. for example, docker run ngnix command will create an instance from the image. if the image is not present on the host, it will try to get a copy of image from docker hub if it is available there.**

You can also run docker run command in detach mode by using the option "-d". This will simply run the container in background while you can continue to perform your other tasks.

If you would like to attach to the docker container  later, you can use the command docker attach {container-id}

if you want to name a container specifically, below is the command while running it.

```
   docker run -d --name {Name} {Image-name}
```

By default, docker run command will run the latest version of the image available in docker hub. if you would like to use a different version, then the tag needs to be specified.

```
docker run {image-name}:{tag}
Example : docker run redis :4.0
```
Docker containers does not listen to a standard input, The docker containers run in a non-interactive mode & it does have a terminal attached. So typically docker containers should be run with a -tf option to be interactive and terminal attached.

**docker ps:** The docker ps commands lists all running containers & some basic information about them. using the docker ps with -a option will show all previously stopped & exited containers

**docker stop:**  The docker stop {container-id} will stop the container, the container ID needs to be provided as argument.

**docker rm :** The remove a container permanently, we can use the docker rm {container-id} command. 

**docker images :** we can use the docker images command to list the docker images on our host.

**docker rmi**  We can use the docker rmi {image-name} command to remove an image from the system. it has to be noted that no containers should be running based out of this image.

**docker pull:**  the docker pull {image-name} will only download the image from docker hub but will not create a container out of it.

Let's say, we were to create a docker container for the ubuntu image with the docker run ubuntu command. It will run the instance of ubuntu & exists immediately. The reason for this is because containers are not meant to host operating systems. Containers are meant to run a specific task such as to host an instance of web server, or an instance of database or simply to carry some kind of computational or analysis task. Once the task is complete, the container will exit. 

Ubuntu operating system once starts does not run any service. Hence it will exit. We can pass or append additional commands such as below

```
docker run ubuntu sleep 5 
```
If you want to execute a command on a running container, this is the format:

docker exec {image-name} {command}
Example : docker exec {image-name} cat /etc/hosts

**Docker Run - Port Mapping :** 
When we run a containerized application, how does the user access the application ? Every docker container gets its own IP by default. This IP is only accessible from the docker Host.

If users want to access the application, they can access it using the Host IP address. But the port that user is trying on should be mapped to the port number on the container.

**Example :** Let us say that there is a docker container which is running on a host with the IP address 192.168.1.1. The application inside the docker container is running on port 5000 & the user from outside is trying to access the application on port 80 with the host IP address. Then there should be a mapping created between the port numbers.

This way, you can run multiple instances of the docker containers & map them to different ports on the host.

```
docker run -p {host-port}:{Container port} {image-name}
```

**How does Docker Store Data :** 

Docker containers have their own file system & any changes to any file are local to the container. As soon as you remove the container all the data inside the container is gone. If you want to retain the data when the container is deleted, you would need to map the data to a directory outside the container on the host.
```
docker run -v {directory-outside}:{directory-inside} {image-name}
Ex: docker run -v /opt/datadir: /var/mysql mysql
```

**See additional details about the container :** 

This command returns details about a specific container in Json format.
```
docker inspect {container-name}
```

**View logs of container :** 

Use the below command to view logs related to a container. You have to run the container with the option "-d" & run it in a detached mode to view the logs relating to it on the host.

```
docker logs {container-name}
```
