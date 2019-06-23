### Building the docker image

In order to build the docker image for this project, at the root of the project, execute the following command:

```shell
docker build -t cebd1160-project-hamza .
```

### Running the docker container using the image built

In order to run a container for the image previously built (Note that this is a short-lived container), please execute the following command:

```shell
docker run cebd1160-project-hamza
```

Note that when you do this, after the execution, the container exits but is still in there (You can see the container with the command `docker ps -a`) in order to clean it up, you need to use the command `docker rm`, or if you don't want to do this, use the tag `--rm` while running it; this would look like:

 ```bash
docker run --rm cebd1160-project-hamza
 ```