#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import thread
import httplib
import requests


# list_dict = sys.argv[2]

def scan(target, dict_path):
    # print host
    f = open("%s" %dict)
    url_list = f.readlines()
    # print url_list
    for line in url_list:
        url = host + line.replace('\n', '')
        r = requests.head("http://%s" % url)
        if r.status_code == 200:
            lock.acquire()
            print "%s | %s" % (url, r.status_code)
            lock.release()
            return url, r.status_code
        else:
            print "dfads"
            # print r.status_code
    f.close()


def scaning(target, dict):
    print 'Start Scan Target: %s' % target
    thread.start_new_thread(scan, (target, dict))
    print "Finished.\n"
    time.sleep(5)

if __name__ == '__main__':
    host = sys.argv[1]
    dict = sys.argv[2]
    lock = thread.allocate_lock()
    scaning(host, dict)
    # scan(host, dict)

