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

### TODO
- Friend list
- Support for others fortune cookies websites
- Support for others e-mail servers (gmail only for now)

### Remarks
If you are going to implement multiple e-mails servers, please follow parsers "architecture"
