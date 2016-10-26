#!/usr/bin/python
# -*- coding: utf-8 -*-
##Author: Amos Lin
##Date: data
##Purpose:purpose
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
    #print "%s-%s-%s" % (h['name'], h['version'], h['release'])

    #compare rpm list
   # if h['name'] in target.get('NAME'):
   #    print target['VERSION'], h['version']

    flag=0
    for item in target:

#       print item
        if h['name'] == item['NAME']:
          flag=1
          #print h['name'], "is equal"
          if h['version']== item['VERSION']:
              #print "source",h['version'],"===",h['release']
               pass
          else:
              print "not eqal"
              print "    ",h['name'],"===",item['NAME']
              print "    ",h['version'],"===",item['VERSION']
              print "    ",h['release'],"===",item['RELEASE']

    if flag==0:

        print "====",h['name'],"not in target"
