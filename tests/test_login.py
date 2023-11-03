#! /usr/bin/python3
# -*- coding: utf-8 -*-
# tests/test_login.py
# Part of test, a package providing testing password verification mechanism.
#
# Copyright © 2023 trong0dn

""" Unit test for 'login' module.
    """

import unittest
import app.login as login


def setup_fixtures(testcase):
    """ Set up fixtures for test cases using 'login'. """
    pass

class Test_Login(unittest.TestCase):
    """ Test case for the login module. """

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