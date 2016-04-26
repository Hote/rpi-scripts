# -*- coding: utf-8 -*-
import sys
import fabric
from fabric.operations import local as lrun
from fabric.api import run, env, sudo
from fabric.context_managers import settings
#from ilogue.fexpect import expect, expecting, run
#import ilogue.fexpect as ft
import paramiko
import socket
import logging
import re
import os
import re
## disable ssh known hosts
env.disable_known_hosts = True

env.user='user'
env.password = 'pwd'

#RESULT_PATTERN = re.compile(r'(\d+).0%', re.M)
RESULT_PATTERN = re.compile(r'(\d+.\d+.\d+.\d+)', re.M)



def localhost():
        env.run = lrun
        env.hosts = ['localhost']

def get_nodeip():
        nodes=[]
        for i in xrange(1,3):
                print "docker  -H cl-master:2378 info| awk $1 == cl-node-%s:" % i
                result=os.popen("docker  -H cl-master:2378 info| grep cl-node-%s:" % i).read()
                match=RESULT_PATTERN.search(result)
                nodes.append(match.group(1))
        for i in nodes:
                env.hosts.append(i)
def all():
        env.hosts = ['cl-master','cl-node-1','cl-node-2']

def shutdown():
    with settings(warn_only=True):
        sudo ("shutdown -h now")

def ex_cmd():
    with settings(warn_only=True):
        sudo ("ifconfig")