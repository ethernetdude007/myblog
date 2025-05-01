---
title: Deploying our first application with Docker
tags:
  - ethernetdude
  - Docker
---
We are going to deploy the Voting app using Docker. It has to be noted, that this application is not written by me & I am simply using an app that is available in GitHub. 

The application is available on this URL : [Click Here
](https://github.com/dockersamples/example-voting-app.git)

I am going to download this application to my ubuntu machine.

```
git clone https://github.com/dockersamples/example-voting-app.git
```
!![Image Description](/images/Pasted%20image%2020250429205638.png)

Now, if you navigate inside the vote directory, you will notice a dockerfile using which we are going to build a docker image.

```
sudo docker build . -t voting-app
```

Now, let us create a container from the image for the voting-app . I am mapping port 5000 to port 80 so that it can be accessed externally.

```
docker run -d -p 5000:80 voting-app
```

Now, if I try the url, I can access the application but if I try to vote. I will get an Internal server error as there is no redis instance linked to this. Below is the screenshot of the Voting App.

!![Image Description](/images/Pasted%20image%2020250429210905.png)

Now I am going to run a container for redis & name it as redis

```
docker run -d --name=redis redis
```

Now, I am going to run the voting application again & link the redis container to it using the below command.

```
docker run -p 5000:80 --link redis:redis voting-app
```

Now, when i try to cast the vote, i don't get an error & get a ticket mark instead as redis is running.

Now, before we run the Worker app, postgres is mandatory. so we have to run a container for postgresql. it should be noted that the -e POSTGRES_HOST_AUTH_METHOD=trust should only be used in lab

```
docker run   -d -e POSTGRES_HOST_AUTH_METHOD=trust --name=db  postgres:15-alpine
```

Now navigate to the worker directory & build the worker image using the dockerfile 

```
docker build . -t  worker-app
```

The worker-app will require 2 links, one with redis & another with postgresql.

```
docker run -d --link redis:redis --link db:db --name=worker-app worker-app
```

Now go to the result-app directory & build the docker image using the docker file.

```
docker build . -t result-app
```

Run the docker image & do the port-mapping and link it to the postgresql db.

```
docker run -d -p 5001:80 --link db:db result-app
```

Now I can see all my containers running & whenever I cast my vote, the result in the application changes.

!![Image Description](/images/Pasted%20image%2020250429223852.png)

**Deploying the same application using Docker-Compose:**

Now, let us see how we can deploy the same application stack using docker compose. You have to install docker compose, separately. The instructions for installing docker compose can be found on docker hub.

```
redis:
  image: redis


dB:
  image: postgres:15-alpine


vote:
  image: voting-app
  ports:
    - 5000:80
  links:
    - redis

worker:
  image: worker:app
  links:
    - redis
    - dB

result:
  image: result-app
  ports:
    - 5001:80
  links:
    - dB
```

the same with the newer version can be written as below. It has to be noted that docker version 3 does not require you to specify the links.

```
version: "3"
services:

  redis:
    image: redis


  db:
    image: postgres:15-alpine
    environment:
      -  POSTGRES_HOST_AUTH_METHOD=trust


  votes:
    image: voting-app
    ports:
      - 5000:80

  result:
    image: result-app
    ports:
      - 5001:80

  worker:
    image: worker-app
```

Now, I am going to run the docker-compose up command & the containers should be created & I should be able to run the app & I can see the result as I casted my vote to Cats.

!![Image Description](/images/Pasted%20image%2020250501045644.png)
