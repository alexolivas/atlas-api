#!/bin/bash
CACHE_DIR=/usr/local/bin/heroku

mkdir -p ${CACHE_DIR}
if [ -d "${CACHE_DIR}" ]; then
    echo "heroku cli already installed"
else
    curl https://cli-assets.heroku.com/install.sh | sh
fi