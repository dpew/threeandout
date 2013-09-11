#!/bin/bash

BASE_DIR=`dirname $0`

echo ""
echo "Starting Karma Server (http://karma-runner.github.io)"
echo "-------------------------------------------------------------------"

export PHANTOMJS_BIN=$HOME/phantomjs/bin/phantomjs
karma start $BASE_DIR/../config/karma2.conf.js $*
