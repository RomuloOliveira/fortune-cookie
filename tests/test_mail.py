#!/bin/env python
# -*- coding: utf-8 -*-

import unittest

from mail import *

class TestMailServers(unittest.TestCase):
    def test_gmail(self):
        email = 'email@gmail.com'
        password = 'pass'

        m = mailer.Mailer(email, password)

        self.assertIsNotNone(m)
        self.assertIsInstance(m, mailer.Mailer)

        self.assertEqual(m.user, email)
        self.assertEqual(m.password, password)

        self.assertEqual(m.config['host'], 'smtp.gmail.com')
        self.assertEqual(m.config['port'], 587)
        self.assertEqual(m.config['tls'], True)

    def test_raise(self):
        email = 'email@foobar.com'
        password = 'pass'

        with self.assertRaises(factory.EmailServerNotFound) as cm:
            m = mailer.Mailer(email, password)