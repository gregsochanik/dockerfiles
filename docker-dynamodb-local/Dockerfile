FROM anapsix/alpine-java:8

# Create working space
RUN mkdir /var/dynamodb_wd
WORKDIR /var/dynamodb_wd

# Default port for DynamoDB Local
EXPOSE 8000

# Get the package from Amazon
RUN wget http://dynamodb-local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest.tar.gz
RUN tar xzf dynamodb_local_latest.tar.gz
RUN rm dynamodb_local_latest.tar.gz

# Default command for image
ENTRYPOINT ["java", "-Djava.library.path=.", "-jar", "DynamoDBLocal.jar", "-dbPath", "/var/dynamodb_local"]
CMD ["-port", "8000"]

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME ["/var/dynamodb_local", "/var/dynamodb_wd"]
