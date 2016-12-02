### aws-cli docker container

This is a containerised version of the AWS cli for use in our builds, as currently AWS don't have an official one.
This is to stop us needing to rely on a 3rd party public container for aws deployment tasks (e.g. ecr get-login).

#### Deployment

This is to be deployed as a public container to Docker Hub, but the idea is that we can provide tagged versions that can be specified in any build using this.

#### Example usage

```
docker run --rm \
  --env AWS_ACCESS_KEY_ID \
  --env AWS_SECRET_ACCESS_KEY \
  gregsochanik/awscli:1.0.1 s3 ls
```
