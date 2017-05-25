#!/bin/sh

OPTIONS=`python /usr/local/bin/mongouri`

if [ -z ${BACKUP_NAME+x} ]; then
  BACKUP_NAME="${MONGO_COLLECTION}_$(date -u +%Y-%m-%d_%H-%M-%S)_UTC.json.gz"
fi

# Run backup
mongoexport ${OPTIONS} | gzip | aws s3 cp -  "s3://${S3_BUCKET}/${S3_PATH}/${BACKUP_NAME}"
