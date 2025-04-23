---
title: Basic Docker Commands
---
**docker run :** The docker run command is used to create a container from an image. for example, docker run ngnix command will create an instance from the image. if the image is not present on the host, it will try to get a copy of image from docker hub if it is available there.

You can also run docker run command in detach mode by using the option "-d". This will simply run the container in background while you can continue to perform your other tasks.

If you would like to attach to the docker container  later, you can use the command docker attach <container-id>

**docker ps:** The docker ps commands lists all running containers & some basic information about them. using the docker ps with -a option will show all previously stopped & exited containers

**docker stop:**  The docker stop <container-id> will stop the container, the container ID needs to be provided as argument.

**docker rm :** The remove a container permanently, we can use the docker rm <container-id> command. 

**docker images :** we can use the docker images command to list the docker images on our host.

**docker rmi**  We can use the docker rmi <image-name> command to remove an image from the system. it has to be noted that no containers should be running based out of this image.

**docker pull:**  the docker pull <image-name> will only download the image from docker hub but will not create a container out of it.

Let's say, we were to create a docker container for the ubuntu image with the docker run ubuntu command. It will run the instance of ubuntu & exists immediately. The reason for this is because containers are not meant to host operating systems. Containers are meant to run a specific task such as to host an instance of web server, or an instance of database or simply to carry some kind of computational or analysis task. Once the task is complete, the container will exit. 

Ubuntu operating system once starts does not run any service. Hence it will exit. We can pass or append additional commands such as below

```
docker run ubuntu sleep 5 
```
If you want to execute a command on a running container, this is the format:

docker exec <image-name> <command>
Example : docker exec <image-name> cat /etc/hosts



