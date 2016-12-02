FROM gliderlabs/alpine:3.1
MAINTAINER Greg Sochanik <greg@sochanik.com>

RUN apk-install groff less python py-pip \
    && pip install --upgrade awscli \
    && apk --purge del py-pip \
    && apk --purge del py-setuptools \
    && rm -rf /var/cache/apk/* \
    && rm -rf /tmp/*

VOLUME ${HOME}/.aws

ENTRYPOINT ["aws"]
