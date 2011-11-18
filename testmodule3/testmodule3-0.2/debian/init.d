#!/bin/bash
case $1 in
    start)  sudo -u hazelwire python /usr/share/hazelwire/testmodule3/exploit/server_twisted & ;;
    stop)   kill -9 `cat /usr/share/hazelwire/testmodule3.pid`
            rm -rf /usr/share/hazelwire/testmodule3.pid;;

esac
exit 0
