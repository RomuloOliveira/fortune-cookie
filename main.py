#!/bin/env python
# -*- coding: utf-8 -*-

import cookie_fetcher

from mail import mailer

if __name__ == '__main__':
    url = 'http://www.fortunecookiemessage.com'
    fortune_cookie_message = cookie_fetcher.get_fortune_cookie(url)

    if fortune_cookie_message is not None:
        with mailer.Mailer('youremail@gmail.com', 'yourpassword') as m:
            m.send_mail('yourfriend@gmail.com', 'Daily fortune cookie!', fortune_cookie_message)
