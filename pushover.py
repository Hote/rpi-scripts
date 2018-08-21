#!/usr/bin/python
import ssl
import httplib, urllib
import socket
import fcntl
import struct
import netrc

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

try:
	eth0=get_ip_address('eth0')
except IOError:
	eth0=''
try:
	wlan0=get_ip_address('wlan0')
except IOError:
	wlan0=''



##get username and password from my netrc
Host='api.pushover.net'
secrets=netrc.netrc()
APP_TOKEN=secrets.authenticators(Host)[0]
USER_KEY=secrets.authenticators(Host)[2]

#https://stackoverflow.com/questions/39945702/httplib-httpsconnection-issue-certificate-verify-failed
IP_ADDR="wlan:"+str(wlan0)+"\n"+"eth0"+str(eth0)
conn = httplib.HTTPSConnection("api.pushover.net:443",timeout=5,context=ssl._create_unverified_context())

conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": APP_TOKEN,
    "user": USER_KEY,
    "message": IP_ADDR,
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
