---
title: Docker storage & Networking
tags:
  - Docker
  - ethernetdude
---
**Docker Storage:** When you install docker on a machine it creates a folder structure under /var/lib/docker. This will have multiple sub folder. all the files related to containers are stored under /var/lib/docker/containers & all the files related to images are stored under /var/lib/docker/images folder.

If you remember from the notes about [[Creating your own docker images]] we learnt that docker builds images in a layered architecture.

Since each layer only stores the changes from the previous layer, it is reflected on the size a well. 

Let's say we have 2 different applications & the images are created from different docker files. Let's say if both the images use the same ubuntu as base layer, Python as the language the code is written, Docker is not going to build them again. It uses the same layers it created before & only changes the information that has changed. 


| ==Application 1==                   | ==Application 2==                   |
| ------------------------------- | ------------------------------- |
| ==Layer1: Ubuntu base image==       | ==Layer1: Ubuntu base image==       |
| ==Layer2: Changes in Apt packages== | ==Layer2: Change in Apt packages==  |
| ==Layer3: Changes in PIP Packages== | ==Layer3: Changes in PIP Packages== |
| Layer4: Source Code             | Layer4: Source Code             |
| Layer5: Update Entrypoint       | Layer5: Update Entrypoint       |
The first three layers are same for both applications. Hence docker does not repeat the process of building the first three layers, hence saving time & space.

All these layers are created when we use the docker build command to form the final image. Once the image is built, these are fixed & becomes read only. The only way to modify them is by initiating a new build.

==When you create a docker container, docker creates a new writable layer on top of the image layer. This layer is used by docker to store data created by the container, any files modified by the user, logs etc.. The life of this layer is only as long as the container is alive.==

Now let us say that I want to modify a piece of code and test a new feature or something. Does this mean I cannot modify the code in a running container ? No, you can still modify and test but docker will not change the image instead will create a new copy of the file on the running container from the image which can be modified.

The data on a container will be destroyed when a container is destroyed. if you wish to store the information created by the container then you will have to use the command mentioned below. This will mount the volume to /var/lib/docker/volumes/{volume-name}

```
docker volume create {volume-name}
```

Later, when you create another container, you can attach this volume using the -V option to the docker run command

```
docker run -v {volume-name}: /var/lib/ {image-name}
```

Lets say we have an external storage on the host and we would like to store the data there instead of the default folder. In that case, we have to specify the complete path.

```
docker run -v /data/{folder-name} : /var/lib/{folder-name} {image-name}
```

The storage drivers are responsible for performing these operations. The drivers available on the host depends on the operating system. 

Few names of storage drivers are as follows, AUFS, ZFS,BTRFS, Overlay & Overlay 2. In case of ubuntu the storage driver is AUFS, in case of Fedora it is ZFS

Docker will automatically choose the storage driver automatically. To find out what storage driver you can use the `docker info` command.