#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

sys.path.append("../client/python")

from cauth import client

lineage = client.study.lineage("7debf7a2-d66c-4c97-a15a-8eeaaf4154ed")

for node in lineage["nodes"]:
    print lineage["nodes"][node]["level"], lineage["nodes"][node]["description"]
 
