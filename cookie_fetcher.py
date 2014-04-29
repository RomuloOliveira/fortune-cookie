#!/bin/env python
# -*- coding: utf-8 -*-

import requests
import xml.etree.ElementTree as ET

from parsers import fortunecookiemessage, factory

def get_fortune_cookie(url):
    r = requests.get(url)

    if r.status_code == 200:
        parser = factory.get_parser(url)

        parser.feed(r.text)

        return parser.get_cookie_message()

    return None
