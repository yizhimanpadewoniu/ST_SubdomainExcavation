#!/usr/bin python
# -*- encoding: utf-8 -*-

import os
import time

from common.utils import init_target


def start(args):
    target = args.target
    target = init_target(target)


def get_domain_type(domain):
    if is_ip(domain):
        return 'ip'
    elif is_url(domain):
        return 'domain'
    else:
        return False