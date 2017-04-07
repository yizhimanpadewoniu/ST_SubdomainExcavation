#!/usr/bin python
# -*- encoding: utf-8 -*-

import re
import urlparse


def is_ip(ip_str):
    ip_regx = """
            ^
            (?:\d{1,2}|1\d\d|2[0-4]\d|25[0-5])
            \.
            (?:\d{1,2}|1\d\d|2[0-4]\d|25[0-5])
            \.
            (?:\d{1,2}|1\d\d|2[0-4]\d|25[0-5])
            \.
            (?:\d{1,2}|1\d\d|2[0-4]\d|25[0-5])
            $
        """

    result = True if re.search(ip_regx, ip_str, re.X) else False
    return result


def init_target(domain):
    ret = domain if domain.find('://') != -1 else 'http://%s' % domain
    return ret
