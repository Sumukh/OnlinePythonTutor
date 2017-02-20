# Python3 Visualizer for unrestricted inputs

# to build:
# docker build -t="pgbovine/cokapi-py3:v1" .
#
# to test:
# docker run -t -i --rm --net=none --cap-drop all pgbovine/cokapi-py3:v1 sh run_tests.sh

FROM python:3.6-slim
# Alpine Linux causes issues with imports in the setup :(
MAINTAINER Philip Guo <philip@pgbovine.net>

RUN mkdir /tmp/python
WORKDIR /tmp/python

# use this to tell python what dependencies to install
ADD requirements.txt /tmp/python
RUN pip3 install -r  /tmp/python/requirements.txt

# Add logger files
ADD pg_logger.py /tmp/python
ADD generate_trace.py /tmp/python
ADD pg_encoder.py /tmp/python
ADD run_tests.sh /tmp/python/run_tests.sh

