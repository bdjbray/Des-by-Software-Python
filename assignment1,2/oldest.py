#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#copyright 2019 Dingjun Bian braybian@bu.edu
"""
Created on Mon Sep 16 16:11:17 2019

@author: ece-student
"""

from sys import argv
from os import listdir, stat

list1=listdir()
l=len(list1)
filelist=[]
for i in range(0,l):
    filelist.append(list1[i])
timelist=[]
for j in range(0,l):
    statinfo = stat(list1[j])
    timelist.append(statinfo[8])
combine=dict(zip(timelist,filelist))
newtimelist=sorted(timelist)
combine_new=(sorted(combine.items(), key=lambda x: x[0]))
b = [i[1] for i in combine_new]
x=argv
m=x[1]
for n in range(0,int(m)):
    print (b[n])
