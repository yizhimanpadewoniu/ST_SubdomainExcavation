#!/usr/bin python
# -*- encoding: utf-8 -*-

from attrdict import AttrDict
from Queue import Queue

fuzz_urls = Queue()

# Result Save
result = AttrDict()
result.fuzz = []
result.brute = []
result.spider = []
