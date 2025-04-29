---
title: Docker Compose
tags:
  - Docker
  - ethernetdude
---
If we want to run a complex application using multiple services, a better way to do it is to use docker compose.

Docker compose is a file written in YAML format. We can put together multiple services running in this file & then use the `docker compose up` command to bring up the entire application stack. It should be noted that this is applicable to containers running on a single host.

Let us look at an example. Let us consider a voting app, which provides an interface for the user to vote & another interface to view the results.

The application consists of different components, the Voting-app written in python allowing the user to vote for  a cat or a dog. when you make a selection, the answer is stored in redis.

This vote is taken by worker an application written in .Net & process the results to a persistent database Postgresql.

Finally, the results of the voting are displayed in a web interface which is an application developed in nodejs.

!![Image Description](/images/Pasted%20image%2020250428185623.png)

Now let us look at how we can put together this application stack on a single docker engine using docker run & docker-compose.

Let us assume that all the images are built & are available in the docker repository. We can run the containers.

```
%% Run the redis image & give it a name. %%
docker run -d --name=redis redis

%% Run the postgres image & give it a name. %%
docker run -d --name=db postgres

%% Run the voting-app & do port mapping to access it externally %%
docker run -d --name =vote -p 5000:80 voting-app

%% Run the result webpage & map it as well %%
docker run -d --name=result -p 5001:80 result-app

%% Run the worker application %%
docker run -d --name=worker worker
```

Even though you run all the container, you will notice that the application will be broken & will not work. The problem here is there is no linking, How will the Voting Web Application know that it has to use this particular instance of redis database.

**Docker run --links :** links is a command line option which can be used to link two containers together.

For example, let us say the Voting app web service is dependent on the redis service. To make the voting app container aware of the redis service, we add the link option.

```
docker run -d --name=vote -p 5000:80 --link redis:redis voting-app
```

This is the reason why have given a name to the container so that we can use the name to create a link.

What infact this does is, to add an entry under the etc/hosts file in the voting app container with the internal IP of the redis container.

**Note :**  It has to be noted that using links in this fashion is being deprecated & might not be supported in future in anymore.

Now let us see how the docker file looks like.

```
redis:
	image: redis
db:
	 image: postgres:9.4
vote:
	image: voting-app
	ports:
		-5000:80
	links:
		-redis
result:
	image :result-app
	ports:
		- 5001:80
	links:
		-db
worker:
	image: worker
	links:
		-redis
		-db
```

In the above example, we are assuming that all the images are already built and are available in the repository. but it is not necessary that be the case.

If we would like to instruct docker compose to build an image instead of pull an image we can replace the image option with build option and specify the location of directory which contain the source code & docker file to build the docker image.


```
redis:
	image: redis
db:
	 image: postgres:9.4
vote:
	**build: ./vote**
	ports:
		-5000:80
	links:
		-redis
result:
	build:./result
	ports:
		- 5001:80
	links:
		-db
worker:
	buid: ./worker
	links:
		-redis
		-db
```


**Docker Compose --Versions:**

Docker compose has seen some developments & now supports more features than the ones before. The latest version of docker-compose is 3. However, we will talk about this in detail later when we talk about docker swarms.

Lets's now talk about difference between docker version 1 & 2

| Docker version 1                                              | Docker Version 2                                                                  |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Version 1 does not have a method to specify dependencies      | Version 2 lets you declare dependencies with a depends_on tag.                    |
| no need to specify the version on top of the file             | Version 2 needs to be specified on the top of the file                            |
| All the containers that run bridge to default network         | Docker automatically creates a dedicated bridge network for the application.      |
| need to use links to enable communication between containers. | All containers are able to communicate with each other using their service names. |












