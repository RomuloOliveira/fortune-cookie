#!/bin/env python
# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser

class BaseCookieParser(HTMLParser):
    def get_cookie_message(self):
        raise NotImplementedError