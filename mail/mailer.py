#!/bin/env python
# -*- coding: utf-8 -*-

import smtplib

import factory

class Mailer():
    def __init__(self, user, password):
        self._stmp_server = None
        self.user = user
        self.password = password

    def __enter__(self):
        self.connect(self.user, self.password)
        return self

    def __exit__(self, type, value, traceback):
        self.disconnect()

    def connect(self, user, password):

        config = factory.get_mailer_config(user)

        self._stmp_server = smtplib.SMTP(config['host'], config['port'])

        if config['tls']:
            self._stmp_server.starttls()

        self._stmp_server.login(user, password)

    def disconnect(self):
        self._stmp_server.close()

    def send_mail(self, to, subject, text):
        message = 'To:{}\nFrom:{}\nSubject: {}\n{}'.format(to, self.user, subject, text)

        self._stmp_server.sendmail(self.user, to, message)