#!/bin/env python
# -*- coding: utf-8 -*-

servers_map = {
    'gmail': {
        'host': 'smtp.gmail.com',
        'port': 587,
        'tls': True
    }
}

class EmailServerNotFound(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

def _extract_name(email):
    first_dot = email.find('@')
    second_dot = email[first_dot+1:].find('.')

    return email[first_dot+1:first_dot+second_dot+1]


def get_mailer_config(email):
    server = _extract_name(email)

    if server not in servers_map:
        raise ParserNotFound('Email server {} not found'.format(server))

    return servers_map[server]
