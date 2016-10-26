#!/usr/bin/python
# -*- coding: utf-8 -*- 
##Author: Amos Lin
##Date: 2016/09/20
##Purpose:compare rpm list with csv file
##[Todo]
import rpm
import csv
import time
# read target rpm list

target=[]
source={}
f=open('rpmlist.csv','r')
#cover csvreader to dictionary
for row in csv.DictReader(f):
        target.append(row)
f.close()



print target
#import operator import itemgetter, attrgetter
ts = rpm.TransactionSet()
mi = ts.dbMatch()
for h in sorted(mi, key=lambda x:x['name']):
    print "%s-%s-%s" % (h['name'], h['version'], h['release'])

    #compare rpm list
   # if h['name'] in target.get('NAME'):
   #    print target['VERSION'], h['version']

    flag=0
    for item in target:
#       print item
        if h['name'] == item['NAME']:

          print h['name'], "is equal"
          print "source",h['version'],"===",h['release']
