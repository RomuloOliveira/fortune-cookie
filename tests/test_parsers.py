#!/bin/env python
# -*- coding: utf-8 -*-

import unittest

from parsers import *

class TestParsers(unittest.TestCase):
    def test_fortune_cookie_message(self):
        url = 'http://www.fortunecookiemessage.com'
        parser = factory.get_parser(url)

        self.assertIsNotNone(parser)
        self.assertIsInstance(parser, fortunecookiemessage.FortuneCookieMessageParser)
