#!/bin/env python
# -*- coding: utf-8 -*-

import base_parser

class FortuneCookieMessageParser(base_parser.BaseCookieParser):

    _message = None

    _cookie_tag = False

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            dict_attrs = dict(attrs)
            if 'class' in dict_attrs and dict_attrs['class'] == 'cookie-link':
                self._cookie_tag = True

    def handle_endtag(self, tag):
        self._cookie_tag = False

    def handle_data(self, data):
        if self._cookie_tag:
            self._message = data

    def get_cookie_message(self):
        return self._message
