[![Stories in Ready](https://badge.waffle.io/romulooliveira/fortune-cookie.png?label=ready&title=Ready)](https://waffle.io/romulooliveira/fortune-cookie)

Daily Fortune Cookie
====================

Send a fortune cookie message to your friend! Inspired by [@tuannyharumi](https://github.com/tuannyharumi) (and "Salmo do Dia").

### Purpose
I started this project as a joke, but it turned out that it has potential and I will use it on examples in my (future) dev blog.

### Requirements
- [Requests 2.2.1](http://docs.python-requests.org/en/latest)  
If you like, you can install all requirements with `sudo pip install -r requirements.txt`

### How to run
Setup your e-mail, your password and friend e-mail in `main.py` and run:  
`python main.py`

### How to implement a new parser
1. Create a class in `parsers/` extending from `BaseCookieParser`
2. Add host name (e.g. `fortunecookiemessage` from "www.fortunecookiemessage.com") to `parsers_map` in `parsers/factory.py`
3. Add module name to `__all__` in `parsers/__init__.py`
4. Add test case in `tests/test_parsers.py`

### How to add support to a new email server
1. Create an dict entry in `servers_map` in `mail/factory.py` containing `host`, `port` and `tls`
2. Add test case in `tests/test_mail.py`

