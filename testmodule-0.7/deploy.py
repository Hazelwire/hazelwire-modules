#!/usr/bin/python

import sys

if sys.argv[1] == "deploy":
    flag = open('/usr/share/hazelwire/testmodule1/exploit/flag.txt','w')
    flag.write(sys.argv[2]+'\n')
    flag.write(sys.argv[3])
    flag.close()

