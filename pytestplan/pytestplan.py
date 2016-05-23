#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools
import json

from pprint import pprint
from settings import settings


def load_conf():
    '''Loads the config file specified in the settings file.'''

    test_conf_file = settings.test_conf_file
    with open(test_conf_file, 'r') as f:
        test_conf = json.load(f)

    return test_conf


def gen_plan():
    '''Creates a test plan based off the test configuration.'''

    test_conf = settings.test_conf
    test_plan = {
        "num_chars": 0,
        "num_tests": 0,
        "test_cases": []
    }

    test_plan["num_chars"] = len(test_conf["characteristics"])

    vals_list = []

    for chars in test_conf["characteristics"]:
        c_name = chars['name']
        vals = [c_name + ' is ' + val for val in chars['values']]
        vals_list.append(vals)

    test_vals = list(itertools.product(*vals_list))
    test_plan['num_tests'] = len(test_vals)
    test_plan['test_cases'] = test_vals
    return test_plan


def output_plan(test_plan):
    '''Outputs the test plan.'''

    print('Test Plan')
    print('='*9)

    for i, tc in enumerate(test_plan['test_cases']):
        print('TC%i: %s' % (i, tc))


def main():
    '''Main class for the phishstorm analytic.'''

    settings.test_conf = load_conf()
    test_plan = gen_plan()
    output_plan(test_plan)


if __name__ == '__main__':
    main()
