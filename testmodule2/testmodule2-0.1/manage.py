#!/usr/bin/python

import sqlite3, sys, os

if sys.argv[1] == 'deploy':
    flag = sys.argv[2]
    db = sqlite3.connect("/usr/share/hazelwire/testmodule2/exploit/entries.sqlite")
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY, name TEXT, text TEXT);")
    c.execute("CREATE TABLE IF NOT EXISTS flag (flag TEXT);")
    c.execute("INSERT INTO flag VALUES (?)",[flag])
    c.close()
    db.commit()
    db.close()
    os.system("chown www-data:www-data /usr/share/hazelwire/testmodule2/exploit/entries.sqlite")
