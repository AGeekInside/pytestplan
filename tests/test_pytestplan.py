#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from pytestplan import pytestplan
from pytestplan.settings import settings

"""
test_pytestplan
----------------------------------

Tests for `pytestplan` module.
"""


class TestPytestplan(unittest.TestCase):

    def setUp(self):
        settings.test_conf_file = 'conf/test_conf.json'

    def tearDown(self):
        pass

    def test_conf_load(self):
        '''Tests the loading of the configuration file.'''

        test_conf = pytestplan.load_conf()
        assert 'characteristics' in test_conf

    def test_plan_gen(self):
        '''Tests the generaion of a simple test plan'''
        settings.test_conf = pytestplan.load_conf()
        test_plan = pytestplan.gen_plan()

        assert 'test_cases' in test_plan
        assert test_plan['num_chars'] == 2
        assert test_plan['num_tests'] == 6


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
