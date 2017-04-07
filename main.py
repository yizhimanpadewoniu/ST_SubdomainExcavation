#!/usr/bin python
# -*- encoding: utf-8 -*-

import sys

from conf.settings import START_STR


def main():
    print START_STR
    try:
        from code.parser import parse
        from code.control.controller import start

        args = parse()
        start(args)
    except Exception, e:
        print e
        import traceback
        traceback.print_exc()
        sys.exit()


if __name__ == '__main__':
    main()
