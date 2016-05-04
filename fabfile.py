# -*- coding: utf-8 -*-
import sys
import fabric
from fabric.operations import local as lrun
from fabric.api import run, env, sudo, cd, put
from fabric.context_managers import settings
import ilogue.fexpect as ft
import paramiko
import socket
import logging
import re
import netrc
import subprocess
## disable ssh known hosts
env.disable_known_hosts = True


env.user='user'
env.password = 'pwd'

#RESULT_PATTERN = re.compile(r'(\d+).0%', re.M)
RESULT_PATTERN = re.compile(r'(\d+.\d+.\d+.\d+)', re.M)


##get username and password from my netrc
secrets=netrc.netrc()
env.user=secrets.authenticators('fabric.raspberry')[0]
env.password=secrets.authenticators('fabric.raspberry')[2]

def localhost():
        env.run = lrun
        env.hosts = ['localhost']

def get_nodeip():
        cmd=" docker -H 192.168.200.1:2378 info|grep cl|awk \'{split($2,ip,\":\");print ip[1]}\'"
        proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=None,shell=True)
        nodes = filter(lambda x:len(x)>0,(line.strip() for line in proc.stdout))
        #print nodes
        for node in nodes:
                env.hosts.append(node.rstrip())

def rpi_update():
    '''do rpi-update '''
    prompts = []
    prompts +=ft.expect('(y/N)','y')

    with ft.expecting(prompts):
            ft.run('rpi-update')
def apt_update():
    '''
    do apt-get update && apt-get upgrade
    '''
    with settings(warn_only=True):
        sudo ("apt-get update")

    prompts = []
    prompts +=ft.expect('(y/N)','y')
    with ft.expecting(prompts):
            ft.run('apt-get upgrade')

def backup_img():
    with cd('tmp'):
        put('/home/rpi-scripts/backup_bz2.sh','/tmp')
        sudo('/bin/bash backup_bz2.sh')

def pre_backup():
    '''install necessary modules for backup'''
    
    prompts = []
    prompts +=ft.expect('(y/N)','y')
    with ft.expecting(prompts):
            ft.run('apt-get install cifs-utils')
            ft.run('atp=get install dosfstools')
            ft.run('atp=get install dump')
            ft.run('atp=get install parted')
            ft.run('atp=get install kpartx')
            
        

def all():
        env.hosts = ['cl-master','cl-node-1','cl-node-2']

def shutdown():

    ## need to remember to shutdown the server last
    env.exclude_hosts=['192.168.200.1']
    with settings(warn_only=True):
        sudo ("shutdown -h now")


def ex_cmd():
    with settings(warn_only=True):
        sudo ("ifconfig")