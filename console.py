#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import code
sys.path.append("../client/python")
from cauth import client, service

if len(sys.argv) > 1:

    if sys.argv[1] == "-r":
        try:
            client.admin.restart()
            exit()
        except:
            pass

else:
    code.interact(banner="Use the 's' object for remote server connection to %s" % service, local={"s": client})
