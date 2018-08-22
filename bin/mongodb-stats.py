# -*- coding:utf-8 -*-

import ConfigParser
from sys import argv

conf=argv[1]

#conf='mytest.txt'
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.read(conf)
sections= config.sections()
mongo_user=config.get('defaults','mongo_user')
sections.remove('defaults')
for section in sections:
    mongo_host=config.get(section,'mongo_host')
    mongo_port = config.get(section, 'mongo_port')
    mongo_pwd = config.get(section, 'mongo_pwd')
    cmd="/bin/bash /usr/local/bin/mongodb-stats.sh {0} {1} {2} {3} {4}".format(mongo_host,mongo_port,mongo_user,mongo_pwd,section)
    #print(cmd)
