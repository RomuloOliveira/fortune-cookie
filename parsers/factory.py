#!/bin/env python
# -*- coding: utf-8 -*-

import urlparse

from . import * # import all parsers

parsers_map = {
    'fortunecookiemessage': fortunecookiemessage.FortuneCookieMessageParser
}

class ParserNotFound(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

def _extract_host_name(url):
    hostname = urlparse.urlparse(url).hostname

    first_dot = hostname.find('.')
    second_dot = hostname[first_dot+1:].find('.')

    return hostname[first_dot+1:first_dot+second_dot+1]


def get_parser(url):
    host = _extract_host_name(url)

    if host not in parsers_map:
        raise ParserNotFound('Parser {} not found'.format(host))

    return parsers_map[host]() # new instance
