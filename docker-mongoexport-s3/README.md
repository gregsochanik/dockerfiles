### scheduleable mongoexport-s3 docker container

This allows you to pipe the results of a `mongoexport` query through gzip directly to an s3 bucket of your choosing, either as a one off job or running as a scheduled task via containerized cron

#### Deployment

Deployed as a public container to Docker Hub gregsochanik/mongoexport-s3

#### Example usage

##### One off job with collection specified

```
docker run --rm \
  --env MONGO_URI=mongodb://user:password@server:port/database \
  --env AWS_ACCESS_KEY_ID \
  --env AWS_SECRET_ACCESS_KEY \
  --env S3_BUCKET=MyBucket \
  --env MONGO_COLLECTION=MyCollection \
  gregsochanik\mongoexport-to-s3

```

##### Scheduled job using containerised cron running every day at midnight

```
docker run -d \
  --env MONGO_URI=mongodb://user:password@server:port/database \
  --env AWS_ACCESS_KEY_ID \
  --env AWS_SECRET_ACCESS_KEY \
  --env S3_BUCKET=MyBucket \
  --env MONGO_COLLECTION=MyCollection \
  --env BACKUP_CRON_SCHEDULE=0 0 * * * \
  gregsochanik\mongoexport-to-s3

```
