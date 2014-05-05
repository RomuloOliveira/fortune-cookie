Daily Fortune Cookie
====================

Send a fortune cookie message to your friend! Inspired by [@tuannyharumi](https://github.com/tuannyharumi) (and "Salmo do Dia")

### Requirements
- [Requests 2.2.1](http://docs.python-requests.org/en/latest)  
If you like, you can install all requirements with `sudo pip install -r requirements.txt`

### How to run
Setup your email, your password and friend e-mail in `main.py` and run:  
`python main.py`

### How to implement a new parser
1. Create a class in `parsers/` extending from `BaseCookieParser`
2. Add host name (e.g. `fortunecookiemessage` from "www.fortunecookiemessage.com") to `parsers_map` in `parsers/factory.py`
3. Add module name to `__all__` in `parsers/__init__.py`
4. Add test case in `tests/test_parsers.py`

### How to add support to a new email server
1. Create an dict entry in `servers_map` in `mail/factory.py` containing `host`, `port` and `tls`
2. Add test case in `tests/test_mail.py`

### TODO
- Friend list
- Support for others fortune cookies websites
- Configurable user/pass/friend (JSON?)