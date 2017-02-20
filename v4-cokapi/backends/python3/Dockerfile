# Python3 Visualizer for unrestricted inputs

# to build:
# Use the make file
# $ make
# to test:
# $ make test

FROM python:3.6-slim
# Alpine Linux causes issues with imports in the setup :(
MAINTAINER Philip Guo <philip@pgbovine.net>

RUN useradd netuser

RUN mkdir /tmp/python
WORKDIR /tmp/python

# use this to tell python what dependencies to install
# RUN pip3 install six

# Add logger files
ADD pg_logger.py /tmp/python
ADD generate_trace.py /tmp/python
ADD pg_encoder.py /tmp/python
ADD run_tests.sh /tmp/python/run_tests.sh

