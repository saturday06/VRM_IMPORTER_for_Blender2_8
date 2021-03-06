#!/usr/bin/env python3

"""
# noqa: INP001
"""

import unittest
from os.path import dirname

test = unittest.TestLoader().discover(start_dir=dirname(dirname(__file__)))
runner = unittest.runner.TextTestRunner()
result = runner.run(test)
if not result.wasSuccessful():
    raise Exception("Failed")
