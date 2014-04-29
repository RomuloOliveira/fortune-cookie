Daily Fortune Cookie
====================

Send a fortune cookie message to your friend! Inspired by [@tuannyharumi](https://github.com/tuannyharumi) (and "Salmo do Dia")

### Requirements
None. Uses only builtin python modules

### How to run
Setup your email, your password and friend e-mail in `main.py` and run:  
`python main.py`

### How to implement a new parser
1. Create a class in `parsers/` extending from `BaseCookieParser`
2. Add host name (e.g. `fortunecookiemessage` from "www.fortunecookiemessage.com") to `parsers_map` in `parsers/factory.py`

### How to add support to a new email server
1. Create an dict entry in `servers_map` in `mail/factory.py` containing `host`, `port` and `tls`

### TODO
- Friend list
- Support for others fortune cookies websites
- Configurable user/pass/friend (JSON?)