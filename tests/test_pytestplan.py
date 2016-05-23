#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest

from pprint import pprint
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
        settings.testing_conf = {
            "characteristics": [
                {"name": "c1", "values": ["<1", ">1", "1"]},
                {"name": "c2", "values": ["True", "False"]}
            ]
        }

    def tearDown(self):
        pass

    def test_conf_load(self):
        '''Tests the loading of the configuration file.'''
        test_conf = pytestplan.load_conf()
        assert 'characteristics' in test_conf

    def test_simple_plan_gen(self):
        '''Tests the generaion of a simple test plan'''
        test_plan = pytestplan.gen_plan(settings.testing_conf)
        assert 'test_cases' in test_plan
        assert test_plan['num_chars'] == 2
        assert test_plan['num_tests'] == 6

    def test_overrides_plan_gen(self):
        override_test_conf = {
            "characteristics": [
                {"name": "c1", "overrides": "False",
                 "values": ["True", "False"]},
                {"name": "c2", "values": ["<1", ">1", "1"]}
            ]
        }

        # print("Overrides test config")
        # pprint(override_test_conf)
        overrides_plan = pytestplan.gen_plan(override_test_conf)

        # print('Overrides plan = ')
        # pprint(overrides_plan)
        assert 'test_cases' in overrides_plan
        assert overrides_plan['num_chars'] == 2
        assert overrides_plan['num_tests'] == 4

    def test_multi_overrides_plan_gen(self):
        test_conf_file = 'conf/multi_overrides_conf.json'

        test_conf = pytestplan.load_conf(test_conf_file)
        multi_overrides = pytestplan.gen_plan(test_conf)

        assert 'test_cases' in multi_overrides
        assert multi_overrides['num_chars'] == 3
        assert multi_overrides['num_tests'] == 12

    def test_plan_output(self):
        '''Tests the format of the test plan output.'''
        test_plan = pytestplan.gen_plan(settings.testing_conf)
        pytestplan.output_plan(test_plan)

        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        output = sys.stdout.getvalue().strip()
        num_lines = len(output.splitlines())
        print(output)

        assert output.startswith('Test Plan')
        assert num_lines == 8


if __name__ == '__main__':
    sys.exit(unittest.main())
