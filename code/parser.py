#!/usr/bin python
# -*- encoding: utf-8 -*-

from conf.settings import VERSION
import argparse


VERSION_INFO = 'Version: %s' % VERSION


def parse():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    # group = parser.add_mutually_exiclusive_group(required=True)
    group.add_argument('-t', '--target', dest='target',
                       help='The target website to be scanned.')
    group.add_argument('-thread', '--thread', dest='thread', type=int, default=5,
                       help='Max number of concurrent HTTP requests (default 5)')
    group.add_argument('-A', '--all-dicts', dest='alldicts',
                       help='Use all dicts to scan.default use -A')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-a', '--asp-dict', dest='aspdict',
                       help='Use asp dict to scan the target.')
    group.add_argument('-p', '--php-dict', dest='phpdict',
                       help='Use php dict to scan the target.')
    group.add_argument('-j', '-jsp-dict', dest='jspdict',
                       help='Use jsp dict to scan the target.')
    group.add_argument('-d', '--dir-dict', dest='dirdict',
                       help='Use dir dict to scan the target.')
    group.add_argument('-x', '--aspx-dict', dest='aspxdict',
                       help='Use aspx dict to scan the target.')
    group.add_argument('-mdb', '--mdb-dict', dest='mdbdict',
                       help='Use mdb dict to scan the target.')
    group.add_argument('-w', '--timeout', dest='timeout',
                       help='the value of timeout.')
    group.add_argument('-o', '--output', dest='output',
                       help='File to save result (*.TXT)')
    group.add_argument('-v', '--version', action='version', version=VERSION_INFO)

    args = parser.parse_args()
    return args
