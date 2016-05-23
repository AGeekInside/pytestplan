#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
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

    def test_plan_output(self):
        '''Tests the format of the test plan output.'''
        settings.test_conf = pytestplan.load_conf()
        test_plan = pytestplan.gen_plan()
        pytestplan.output_plan(test_plan)

        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip()
        num_lines = len(output.splitlines())
        print(output)
        assert output.startswith('Test Plan')
        assert num_lines == 8


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
