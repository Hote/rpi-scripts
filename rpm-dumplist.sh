#!/bin/sh

# prepare a CSV of currently installed RPM packages

echo "NAME,VERSION,RELEASE"

rpm -qa --queryformat "%{NAME},%{VERSION},%{RELEASE}\n" | sort -t\; -k 1