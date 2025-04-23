---
title: What is the need for Docker & How they are different from Virtual Machines
tags:
  - Docker
  - ethernetdude
---
Docker lets us run each component in a separate container with its own dependencies & libraries. This let's us run the application irrespective of the operating system we are using.

**What are Containers ?**

Containers are isolated environments, which can have their own processes, network & mounts just like virtual machines except that they all share the same OS kernel.

If you look at operating systems like Ubuntu, Fedora, Centos etc.. They all contain a OS Kernel & Software. The OS kernel is responsible for interacting with the Hardware & Software consists of things like drivers, user interface , etc.. So all these operating systems have the same linux Kernel.

Docker containers share the same common linux kernel. Meaning, Docker containers can run any operating system as long as they share the same kernel. It also means that a docker containers cannot run on windows if the containers themself are running a linux. 

!![Image Description](/images/Pasted%20image%2020250422221202.png)
It also is note worthy, Docker containers are lite as the Kernel is shared & each docker container only needs to have the additional software that makes these operating systems unique.

The Only, reason why you see windows running docker is basically because docker is not directly installed on windows. The linux kernel runs on top of windows as a virtual Machine & which in turn runs Docker.

**Difference between Virtual Machine & Containers :**

This image shows the fundamental difference between Docker & Virtual Machines.

!![Image Description](/images/Pasted%20image%2020250422221928.png)

1. Each Virtual machine has its own operating system. 
2. Virtual Machines are heavy, require more disk space, takes time to boot compared to Docker.
3. Virtual machines have complete isolation from each other as they run different operating systems.

Most organizations today have their applications in a containerized version. Many applications are available in a public repository called "Docker Hub"

You can also create your own container Image if something that is available in public does not fit your need.

If you need multiple instances of a image ( Instance in docker is referred as container ). You can easily scale it up & scale-down when not required.

**Key Takeways:**
1. Docker runs on top of Linux Kernel & doesn't require individual OS per each container like Virtual Machines.
2. You create something called a Docker file with information in it & then convert that into a Docker image & then the image is deployed and a running instance is called as container.

**How to Install Docker :**

The way that you install depends on the operating system you are using. You can find out how to install by going to [docs.docker.com](). In my case, I have a ubuntu Virtual machine running on VmWare Workstation on which I am going to install Docker.

**uninstall any older version of Docker by using the below command :**

```
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

Now, there are multiple ways to install Docker, You can install using the Package manager apt-get or else, there is a script that is given by docker to install everything.

```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh --dry-run
```

```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

Once you do that, you can use the command `"sudo docker version"` to check if it got installed correctly.

!![Image Description](/images/Pasted%20image%2020250423202519.png)