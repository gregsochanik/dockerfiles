FROM gliderlabs/alpine:3.1
MAINTAINER 7digital Tech Team <tech-team@7digital.com>

RUN apk-install groff less python py-pip \
    && pip install --upgrade awscli \
    && apk --purge del py-pip \
    && apk --purge del py-setuptools \
    && rm -rf /var/cache/apk/* \
    && rm -rf /tmp/*

VOLUME ${HOME}/.aws

ENTRYPOINT ["aws"]
