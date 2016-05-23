#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools
import json

from pprint import pprint
from settings import settings


def load_conf(conf_file=settings.test_conf_file):
    '''Loads the config file specified in the settings file.'''

    with open(conf_file, 'r') as f:
        test_conf = json.load(f)

    return test_conf


def gen_tc(C, val):

    return C + " is " + val


def gen_plan(test_conf):
    '''Creates a test plan based off the test configuration.'''

    # print("Generating plan for:")
    # pprint(test_conf)

    test_plan = {
        "num_chars": 0,
        "num_tests": 0,
        "test_cases": []
    }

    test_plan["num_chars"] = len(test_conf["characteristics"])

    vals_list = []
    overrides = []

    for chars in test_conf["characteristics"]:
        if "overrides" in chars:
            overrides.append(gen_tc(chars["name"], chars["overrides"]))
        c_name = chars['name']
        vals = [gen_tc(c_name, val) for val in chars['values']]
        vals_list.append(vals)

    override_found = {override: 0 for override in overrides}
    # if len(overrides) > 0:
    #     print("Outputting the overrides found:")
    #     pprint(overrides)

    #     pprint(override_found)
    #     pprint(overrides)
    # else:
    #     print('No overrides found')

    test_cases = list(itertools.product(*vals_list))
    # pprint(test_cases)

    to_remove = []

    for tc in test_cases:
        for condition in tc:
            if condition in overrides:
                override_found[condition] += 1
                if override_found[condition] > 1:
                    to_remove.append(tc)

    # if len(to_remove) > 0:
    #     pprint(to_remove)
    # else:
    #     print("No test cases to remove.")

    for redundant_tc in to_remove:
        if redundant_tc in test_cases:
            test_cases.remove(redundant_tc)

    test_plan['num_tests'] = len(test_cases)
    test_plan['test_cases'] = test_cases
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
    test_plan = gen_plan(settings.test_conf)
    output_plan(test_plan)


if __name__ == '__main__':
    main()
