### dynamodb-local docker container

This is a containerised version of the AWS Dynamodb local service.

#### Deployment

This is to be deployed as a public container to Docker Hub, but the idea is that we can provide tagged versions that can be specified in any build using this.

#### Example usage

```
docker run -d \
  --publish 8000:8000
  --name dynamodb
  gregsochanik/dynamodb-local:1.0.1 s3 ls
```
