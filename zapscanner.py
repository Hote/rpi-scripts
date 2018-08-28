# Start ZAP in daemon mode with ./zap.sh -daemon

import time
from collections import defaultdict
from random import randrange

from zap import ZAP, ZapError
from prettytable import PrettyTable

# Specify the URL to start the attack
TARGET = "http://victim"

print "Attacking %s with ZAP" % TARGET

zap = ZAP()
zap.urlopen(TARGET)


# Start spidering the site from the specified URL
# Note that the exception here isn't an error, I think
# it's a bug in the client as the content of the error
# says OK
try:
    zap.start_spider(TARGET)
except ZapError, e:
    pass

print "Spidering"

# Wait for the spider to finish
while (int(zap.spider_status['status']) < 100):
    time.sleep(1)


# Start scanning the collected URLs for vulnerabilities
try:
    zap.start_scan(TARGET)
except ZapError, e:
    pass

print "Scanning"

# wait for the scanning to finish
while (int(zap.scan_status['status']) < 100):
    time.sleep(1)

# create a data structure to match our output
sort_by_url = defaultdict(list)
for alert in zap.alerts['alerts']:
    sort_by_url[alert['url']].append({
                                'risk':  alert['risk'],
                                'alert': alert['alert']
                                })

# print a useful set of tables of the alerts
for url in sort_by_url:
    print
    print url

    results = PrettyTable(["Risk", "Description"])
    results.padding_width = 1
    results.align = "l"
    results.sortby = "Risk"

    for details in sort_by_url[url]:
        results.add_row([details['risk'], details['alert']])
    print results
