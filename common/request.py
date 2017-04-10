#!/usr/bin python
# -*- encoding: utf-8 -*-

import sys
import time
import thread
import httplib
import requests
import socket
import logging

from common.threadpool import ThreadPool
from urlparse import urlparse

logger = logging.getLogger('domainfuzz')

class Req(object):
    def __init__(self, site, threads, timeout):
        self.site = site if site.find('://') != -1 else 'http://%s' % site
        self.site_parse = urlparse(self.site)
        self.timeout = timeout
        self.pool = ThreadPool(threads)

    def send_head(self, url):
        u = urlparse(url)
        l = 0
        try:
            conn = httplib.HTTPConnection(u[1], timeout=self.timeout)
            conn.request('HEAD', '')
            l = conn.getresponse()
            logger.info('%s %s' % (url, l.status))
        except (httplib.HTTPException, socket.timeout, socket.gaierror, Exception), e:
            logger.error('url %s is unreachable, Exception %s %s' % (url, e.__class__.__name__, e))
            print "url %s is unreacheable, Exception %s %s" % (url.encode('utf-8'), e.__class__.__name__, e)
            pass
        return l
