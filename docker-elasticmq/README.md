### ElasticMQ docker container

This is a containerised version of the ElasticMQ service, useful for dev testing against AWS SQS.

#### Deployment

This is to be deployed as a public container to Docker Hub, but the idea is that we can provide tagged versions that can be specified in any build using this.

#### Example usage

```
docker run -d \
  --publish 9324:9324
  --name elasticmq
  gregsochanik/elasticmq:1.0.1
```
