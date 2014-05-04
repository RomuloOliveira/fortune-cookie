Daily Fortune Cookie
====================

Send a fortune cookie message to your friend! Inspired by [@tuannyharumi](https://github.com/tuannyharumi) (and "Salmo do Dia").

### Purpose
I started this project as a joke, but it turned out that it has potential and I will use it on examples in my (future) dev blog.

### Requirements
None. Uses only builtin python modules.

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

### TODO
- Friend list
- Support for others fortune cookies websites
- Configurable user/pass/friend (JSON?)
