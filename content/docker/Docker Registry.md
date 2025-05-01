---
title: Docker Resistry
tags:
   - Docker
   - ethernetdude
---
Docker images are stored in the docker registry. When we run a docker command line `docker run ngnix` the image is being pulled from the docker.io library

By default, the library prefix is used indicating an official docker Hub image. However, there is an option for us to create our custom images & store them.

Where we store these images ? we can store these images on cloud provider like google cloud or azure & make them not accessible publicly.

We can also use the docker.io as well & make it private. When trying to access an image from private registry. We must first login to the our docker account using the `docker login` command.

We also have an option to store our images on-prem & deploy own private registry. The docker Registry is itself an application & available as an image.

Simply run the container using the command

```
docker run -d -p 5000:5000 --name registry registry:latest
```

push the newly created image to docker registry:

```
docker image tag {image-name} {registry-container-ip:5000}/image-name

docker push {registry-container-ip:5000}/{image-name}
```

once this is done, I can pull the docker image to any host which has reachability to the registry-container IP using the docker pull command.

```
docker pull {registry-container-ip:5000}/{image-name}
```

it should be noted, that you would need authentication & login to the private registry by using the `docker login {Registry-container-ip}`