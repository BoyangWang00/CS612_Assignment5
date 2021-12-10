#! /usr/bin/bash
set -e -u -o pipefail
cd "$(dirname "$BASH_SOURCE")"

docker build -t test .
echo "STARTING SERVER... "
echo "To view the page, open this=> file://$(realpath Assignment5.html)"
docker run -ti --rm -p 8000:8000 test