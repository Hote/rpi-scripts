##########################################################
# Dockerfile build ruby
# in rasberrypi
############################################################
# Base image to ubuntu:14.04
FROM resin/rpi-raspbian:latest

#Author WHO
MAINTAINER Amos Lin

#update the repository source list
RUN apt-get update
RUN  apt-get install autoconf automake libtool maven
RUN apt-get install pkg-config zip g++ zlib1g-dev unzip
RUN apt-get install python-pip  python-dev
RUN pip install  https://github.com/samjabrahams/tensorflow-on-raspberry-pi/raw/master/bin/tensorflow-0.8.0rc0-cp27-none-linux_armv7l.whl