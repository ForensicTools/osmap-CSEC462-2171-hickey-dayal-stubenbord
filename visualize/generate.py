#!/usr/bin/python

import random

os = ["windows","linux","macosX"]

for i in range(1,254):
    ip="192.168.1."+ str(i)
    osrand=random.randrange(0,len(os))
    oper=os[osrand]
    rand=str(random.randint(100,300))
    print(ip+','+oper+','+rand)


