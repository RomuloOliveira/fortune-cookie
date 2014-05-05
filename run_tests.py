#!/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import unittest
    suite = unittest.TestLoader().discover('./tests')
    unittest.TextTestRunner(verbosity=3).run(suite)