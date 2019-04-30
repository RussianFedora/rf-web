#!/bin/bash

RSH_STRING="/usr/bin/sshpass -p ${DEPLOY_PASSWORD} ssh -o StrictHostKeyChecking=no -l ${DEPLOY_USER}"

HOST="212.227.198.243"
DEST=${TRAVIS_BRANCH:-test}
echo "Publishing to ${DEST}"

rsync -rav --delete --rsh="${RSH_STRING}" output/ ${HOST}:~/"${DEST}"

# Run nikola's post deploy hooks
rsync -rav --delete --rsh="${RSH_STRING}" ${HOST}:~/"${DEST}"/cache cache/ || true
nikola deploy
rsync -rav --delete --rsh="${RSH_STRING}" cache/ ${HOST}:~/"${DEST}"/cache
