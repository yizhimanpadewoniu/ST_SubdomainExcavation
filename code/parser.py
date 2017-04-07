#!/usr/bin python
# -*- encoding: utf-8 -*-

from conf.settings import VERSION
import argparse


VERSION_INFO = 'Version: %s' % VERSION


def parse():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(require=True)
    # group = parser.add_mutually_exiclusive_group(required=True)
    group.add_argument('-t', '--target', dest='target',
                       help='The target website to be scanned.')
    group.add_argument('-a', '--asp-dict', dest='asp-dict',
                       help='Use asp dict to scan the target.')
    group.add_argument('-p', '--php-dict', dest='php-dict',
                       help='Use php dict to scan the target.')
    group.add_argument('-j', '-jsp-dict', dest='jsp-dict',
                       help='Use jsp dict to scan the target.')
    group.add_argument('-d', '--dir-dict', dest='dir-dict',
                       help='Use dir dict to scan the target.')
    group.add_argument('-x', '--aspx-dict', dest='aspx-dict',
                       help='Use aspx dict to scan the target.')
    group.add_argument('-mdb', '--mdb-dict', dest='mdb-dict',
                       help='Use mdb dict to scan the target.')
    group.add_argument('-v', '--version', action='version', version=VERSION_INFO)

    args = parser.parse_args()
    return args
