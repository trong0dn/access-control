#! /usr/bin/python3
# -*- coding: utf-8 -*-
# tests/test_enrolment.py
# Part of test, a package providing testing enrolment mechanism and the proactive password checker.
#
# Copyright © 2023 trong0dn

""" Unit test for 'enrolment' module.
    """

import unittest
import app.enrolment as enrolment


def setup_fixtures(testcase):
    """ Set up fixtures for test cases using 'enrolment'. """
    pass

class Test_Enrolment(unittest.TestCase):
    """ Test case for the enrolment module. """

    def setUp(self):
        """ Set up the test fixtures. """
        setup_fixtures(self)

    
def suite():
    """ Create the test suite for this module. """
    from sys import modules
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(modules[__name__])
    return suite


# Local variables:
# mode: python
# End:
# vim: filetype=python fileencoding=utf-8 :