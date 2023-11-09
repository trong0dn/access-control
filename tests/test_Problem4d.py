#! /usr/bin/python3
# -*- coding: utf-8 -*-
# tests/test_Problem4d.py
# Part of test, a package providing testing password verification mechanism.
#
# Copyright © 2023 trong0dn

""" Unit test for 'login' module.
    """

import unittest
import app.Problem4c as login
from datetime import datetime


def setup_fixtures(testcase):
    """ Set up fixtures for test cases using 'login'. """

    testcase.password = "TwG4v$iLf8%p"
    
    testcase.regular_client = 'regular_client'
    testcase.premium_client = 'premium_client'
    testcase.teller = 'teller'
    testcase.financial_advisor = 'financial_advisor'
    testcase.financial_planner = 'financial_planner'
    testcase.investment_analyst = 'investment_analyst'
    testcase.compliance_officer = 'compliance_officer'
    testcase.technical_support = 'technical_support'

class Test_Login(unittest.TestCase):
    """ Test case for the login module. """

    def setUp(self):
        """ Set up the test fixtures. """
        setup_fixtures(self)

    def test_enforce_access_control_regular_client(self):
        """ Enforce access control on regular client. """
        self.assertTrue(login.enforce_access_control(self.regular_client))

    def test_enforce_access_control_premium_client(self):
        """ Enforce access control on premium client. """
        self.assertTrue(login.enforce_access_control(self.premium_client))

    def test_enforce_access_control_teller(self):
        """ Enforce access control on teller. """
        if ((datetime.now().hour < 8) or (datetime.now().hour > 17)):
            self.assertFalse(login.enforce_access_control(self.teller))
        else:
            self.assertTrue(login.enforce_access_control(self.teller))

    def test_enforce_access_control_financial_advisor(self):
        """ Enforce access control on financial advisor. """
        self.assertTrue(login.enforce_access_control(self.financial_advisor))

    def test_enforce_access_control_financial_planner(self):
        """ Enforce access control on financial planner. """
        self.assertTrue(login.enforce_access_control(self.financial_planner))

    def test_enforce_access_control_investment_analystr(self):
        """ Enforce access control on investment analyst. """
        self.assertTrue(login.enforce_access_control(self.investment_analyst))

    def test_enforce_access_control_compliance_officer(self):
        """ Enforce access control on compliance officer. """
        self.assertTrue(login.enforce_access_control(self.compliance_officer))

    def test_enforce_access_control_technical_support(self):
        """ Enforce access control on technical support. """
        self.assertTrue(login.enforce_access_control(self.technical_support))

    
def suite_login():
    """ Create the test suite for this module. """
    from sys import modules
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(modules[__name__])
    return suite


# Local variables:
# mode: python
# End:
# vim: filetype=python fileencoding=utf-8 :