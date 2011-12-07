#!/usr/bin/python

import sys
import xml.dom.minidom
import os

if sys.argv[1] == 'deploy':
    flag = sys.argv[2]
    f = open("/usr/share/hazelwire/testmodule3/exploit/flag.txt", 'w')
    f.write(flag)
    f.close()

if sys.argv[1] == "configure":
    dom = xml.dom.minidom.parse(os.getenv("MODULEDIR")+"testmodule3/config.xml")
    #The service port is configurable in this module, get it from the XML:
    for option in dom.getElementsByTagName("option"):
        if option.getElementsByTagName("name")[0].childNodes[0].data == "Service port":
            port = option.getElementsByTagName("value")[0].childNodes[0].data
    #Write the port number to a file in the module dir
    f = open("/usr/share/hazelwire/testmodule3/port", "w")
    f.write(port)
    f.close()
