#!/usr/bin/env sh
set -e

service nginx stop
service nginx start

exec "$@"