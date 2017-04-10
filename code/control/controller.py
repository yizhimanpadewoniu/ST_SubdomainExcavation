#!/usr/bin python
# -*- encoding: utf-8 -*-

import os
import time
import logging
from common.utils import init_target
from common.utils import get_host
from common.utils import get_domain_type
from common.log import init_logger
from conf import settings
from code.output.output_txt import OutputTxt

logger = logging.getLogger('domainfuzz')


def init():
    if not os.path.exists(settings.LOG_PATH):
        os.makedirs(settings.LOG_PATH)


def complate(output_file):
    print '\n'
    print 'Ready to write result to %s' % output_file
    logger.info('output result to file ...')
    OutputTxt(output_file).save()
    logger.info('complete!')


def start(args):
    target = args.target
    timeout = args.timeout
    target = init_target(target)
    output = args.output
    domain_type = get_domain_type(target)

    if domain_type in settings.ALLOW_INPUTS:
        init()
        init_logger(log_file_path=settings.LOG_PATH + '/' + get_host(target) + '.log')
        print '[%s] Scan Target: %s' % (time.strftime('%H:%M:%S'), target)
        if output:
            complate(output)
