---
title: Docker Engine
tags:
 - Docker
 - ethernetdude
---
Docker Engine as we discussed before is simply referred to a host with docker installed on it. When we install docker on a machine, three different components are installed.

![[Screenshot 2025-05-01 at 4.32.54 PM.png | 500]]

The docker Deamon is a background process that manages such as images, volumes, containers & networks. The docker rest api is that programs can use to talk to the docker deamon. Docker CLI is the command line interface that we are interacting with.

It is important to understand that the docker CLI need not necessarily be on the same host. It can be on a different remote machine.

```
docker -H={remote-docker-engine:2375}
```

for example, to run a a nginx engine on a remote host. use the following format.

```
docker -H={remote-docker-engine-IP:2375} run nginx
```

Now, let us understand how exactly our applications are containerized in docker. Docker uses, namespaces to isolate work space. Process ID'S unix timesharing, Network, Mount & Interprocess are created in their own name space there by providing isolation between containers.

!![Image Description](/images/Pasted%20image%2020250501173256.png)

let us try to understand one of the namespace isolation technique, process ID. When ever a linux system boots up, it starts with just one process & process ID 1. This is the root process, by the time the system boots up, we will have lot of processes running. The process ID's are unique & 2 processes cannot have the same process ID. Now, if we are running a container in the linux host, lets say nginx, it will boot with a process ID of 1 as well. but in the host operating system point of view, it is not Process ID of 1 & it is referred as just another process with a number.

Docker also uses cggroup to restrict the amount of resources allocated to each container. By default there is no restriction.

if you want to restrict the amount of memory or CPU a container can use. you can use the below commands

```
%%this allocates, 50 percent of the cpu to the container%%
docker run --cpu=.5 {container-name}

%%this allocates 100Mb of memory to the container%%
docker run --memory=100m {container-name}
```
