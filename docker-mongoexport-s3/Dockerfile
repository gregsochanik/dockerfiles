FROM alpine:edge
MAINTAINER Greg Sochanik <greg@sochanik.com>

RUN echo http://dl-4.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories && \
  apk add --no-cache mongodb-tools py2-pip && \
  pip install pymongo awscli

ENV S3_PATH=mongodb
ENV AWS_DEFAULT_REGION=us-east-1

ADD entrypoint.sh /usr/local/bin/entrypoint
ADD backup.sh /usr/local/bin/backup
ADD mongouri.py /usr/local/bin/mongouri

RUN ["chmod", "+x", "/usr/local/bin/entrypoint"]
RUN ["chmod", "+x", "/usr/local/bin/backup"]

CMD /usr/local/bin/entrypoint
