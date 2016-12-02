FROM anapsix/alpine-java:8
MAINTAINER Greg Sochanik <greg@sochanik.com>

RUN mkdir /var/dynamodb_wd
WORKDIR /var/dynamodb_wd

EXPOSE 8000

RUN wget http://dynamodb-local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest.tar.gz && \
  tar xzf dynamodb_local_latest.tar.gz && \
  rm dynamodb_local_latest.tar.gz

ENTRYPOINT ["java", "-Djava.library.path=.", "-jar", "DynamoDBLocal.jar", "-dbPath", "/var/dynamodb_local"]
CMD ["-port", "8000"]

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME ["/var/dynamodb_local", "/var/dynamodb_wd"]
