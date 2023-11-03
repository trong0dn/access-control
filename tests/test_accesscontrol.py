#! /usr/bin/python3
# -*- coding: utf-8 -*-
# tests/test_accesscontrol.py
# Part of test, a package providing testing access control mechanism.
#
# Copyright © 2023 trong0dn

""" Unit test for 'accesscontrol' module.
    """

import unittest
from app.accesscontrol import Access, Resource, Role


def setup_fixtures(testcase):
    """ Set up fixtures for test cases using 'accesscontrol'. """

    testcase.access = [
        ('READ', "<Access.READ: 1>"),
        ('WRITE', "<Access.WRITE: 2>"),
        ('OWN', "<Access.OWN: 3>")
        ]
    testcase.resource = [
        ('account_balance', "<Resource.account_balance: 1>"),
        ('investment_portfolio', "<Resource.investment_portfolio: 2>"),
        ('advisor_contact', "<Resource.advisor_contact: 3>"),
        ('planner_contact', "<Resource.planner_contact: 4>"),
        ('analyst_contact', "<Resource.analyst_contact: 5>"),
        ('consumer_instruments', "<Resource.consumer_instruments: 6>"),
        ('market_instruments', "<Resource.market_instruments: 7>"),
        ('interest_instruments', "<Resource.interest_instruments: 8>"),
        ('derivative_trading', "<Resource.derivative_trading: 9>"),
        ('client_information', "<Resource.client_information: 10>"),
        ('account_access', "<Resource.account_access: 11>")
        ]
    testcase.role = [
        ('regular_client', "<Role.regular_client: {<Resource.account_balance: 1>: [<Access.READ: 1>], <Resource.investment_portfolio: 2>: [<Access.READ: 1>], <Resource.advisor_contact: 3>: [<Access.READ: 1>]}>"),
        ('premium_client', "<Role.premium_client: {<Resource.account_balance: 1>: [<Access.READ: 1>], <Resource.investment_portfolio: 2>: [<Access.READ: 1>, <Access.WRITE: 2>], <Resource.advisor_contact: 3>: [<Access.READ: 1>], <Resource.planner_contact: 4>: [<Access.READ: 1>], <Resource.analyst_contact: 5>: [<Access.READ: 1>]}>, 'teller': <Role.teller: {<Resource.account_balance: 1>: [None], <Resource.investment_portfolio: 2>: [None]}>"),
        ('teller', "<Role.financial_advisor: {<Resource.account_balance: 1>: [<Access.READ: 1>], <Resource.investment_portfolio: 2>: [<Access.READ: 1>, <Access.WRITE: 2>], <Resource.consumer_instruments: 6>: [<Access.READ: 1>]}>"),
        ('financial_advisor', "<Role.financial_advisor: {<Resource.account_balance: 1>: [<Access.READ: 1>], <Resource.investment_portfolio: 2>: [<Access.READ: 1>, <Access.WRITE: 2>], <Resource.consumer_instruments: 6>: [<Access.READ: 1>]}>"),
        ('financial_planner', "<Role.financial_planner: {<Resource.account_balance: 1>: [<Access.READ: 1>], <Resource.investment_portfolio: 2>: [<Access.READ: 1>, <Access.WRITE: 2>], <Resource.consumer_instruments: 6>: [<Access.READ: 1>], <Resource.market_instruments: 7>: [<Access.READ: 1>]}>"),
        ('investment_analyst', "<Role.investment_analyst: {<Resource.account_balance: 1>: [<Access.READ: 1>], <Resource.investment_portfolio: 2>: [<Access.READ: 1>, <Access.WRITE: 2>], <Resource.consumer_instruments: 6>: [<Access.READ: 1>], <Resource.market_instruments: 7>: [<Access.READ: 1>], <Resource.interest_instruments: 8>: [<Access.READ: 1>], <Resource.derivative_trading: 9>: [<Access.READ: 1>]}>"),
        ('compliance_officer', "<Role.compliance_officer: {<Resource.account_balance: 1>: [<Access.READ: 1>], <Resource.investment_portfolio: 2>: [<Access.READ: 1>, <Access.OWN: 3>]}>"),
        ('technical_support', "<Role.technical_support: {<Resource.client_information: 10>: [<Access.READ: 1>], <Resource.account_access: 11>: None}>")
        ]
    
    access_keys = [key for (key, name) in testcase.access]
    resource_keys = [key for (key, name) in testcase.resource]
    role_keys = [key for (key, name) in testcase.role]

    testcase.valid_values = {
        Access: dict(
            keys = access_keys
            ),
        Resource: dict(
            keys = resource_keys
            ),
        Role: dict(
            keys = role_keys
            )
        }

    testcase.other_values = [
        None, 0, 1, (), Access, Resource, Role, "bogus"
        ]


class Test_Access(unittest.TestCase):
    """ Test case for the Access enum class. """

    def setUp(self):
        """ Set up the test fixtures. """
        setup_fixtures(self)

    def test_length(self):
        """ Access enum should have length of its value set. """
        for accesstype, params in self.valid_values.items():
            if (accesstype) == type(list(Access)[0]):
                self.assertEqual(len(params['keys']), len(accesstype))

    def test_value_items(self):
        """ Access enum should have items for each value. """
        for accesstype, params in self.valid_values.items():
            if (accesstype) == type(list(Access)[0]):
                for i, key in enumerate(params['keys']):
                    value = params['keys'][i]
                    test_value = Access._member_names_[i]
                    self.assertEqual(value, test_value)

    def test_iterate_sequence(self):
        """ Access enum iteration should match specified sequence. """
        for accesstype, params in self.valid_values.items():
            if (accesstype) == type(list(Access)[0]):
                values_seq = [key for key in Access._member_names_]
                test_seq = [val for val in accesstype._member_names_]
                self.assertEqual(values_seq, test_seq)
                self.assertNotEqual(values_seq.reverse(), test_seq)   

    def test_membership_bogus(self):
        """ Access enum should not contain bogus values. """
        for accesstype, params in self.valid_values.items():
            if (accesstype) == type(list(Access)[0]):
                for value in self.other_values:
                    self.assertFalse(value in params["keys"])


class Test_Resource(unittest.TestCase):
    """ Test case for the Resource enum class. """

    def setUp(self):
        """ Set up the test fixtures. """
        setup_fixtures(self)

    def test_length(self):
        """ Resource enum should have length of its value set. """
        for resourcetype, params in self.valid_values.items():
             if (resourcetype) == type(list(Resource)[0]):
                self.assertEqual(len(params['keys']), len(resourcetype))

    def test_value_items(self):
        """ Resource enum should have items for each value. """
        for resourcetype, params in self.valid_values.items():
            if (resourcetype) == type(list(Resource)[0]):
                for i, key in enumerate(params['keys']):
                    value = params['keys'][i]
                    test_value = Resource._member_names_[i]
                    self.assertEqual(value, test_value)

    def test_iterate_sequence(self):
        """ Resource enum iteration should match specified sequence. """
        for resourcetype, params in self.valid_values.items():
            if (resourcetype) == type(list(Resource)[0]):
                values_seq = [key for key in Resource._member_names_]
                test_seq = [val for val in resourcetype._member_names_]
                self.assertEqual(values_seq, test_seq)
                self.assertNotEqual(values_seq.reverse(), test_seq)   

    def test_membership_bogus(self):
        """ Resource enum should not contain bogus values. """
        for resourcetype, params in self.valid_values.items():
            if () == type(list(Resource)[0]):
                for value in self.other_values:
                    self.assertFalse(value in params["keys"])


class Test_Role(unittest.TestCase):
    """ Test case for the Role enum class. """

    def setUp(self):
        """ Set up the test fixtures. """
        setup_fixtures(self)

    def test_length(self):
        """ Role enum should have length of its value set. """
        for roletype, params in self.valid_values.items():
             if (roletype) == type(list(Resource)[0]):
                self.assertEqual(len(params['keys']), len(roletype))

    def test_value_items(self):
        """ Role enum should have items for each value. """
        for roletype, params in self.valid_values.items():
            if (roletype) == type(list(Role)[0]):
                for i, key in enumerate(params['keys']):
                    value = params['keys'][i]
                    test_value = Role._member_names_[i]
                    self.assertEqual(value, test_value)

    def test_iterate_sequence(self):
        """ Role enum iteration should match specified sequence. """
        for roletype, params in self.valid_values.items():
            if (roletype) == type(list(Resource)[0]):
                values_seq = [key for key in Resource._member_names_]
                test_seq = [val for val in roletype._member_names_]
                self.assertEqual(values_seq, test_seq)
                self.assertNotEqual(values_seq.reverse(), test_seq)   

    def test_membership_bogus(self):
        """ Role enum should not contain bogus values. """
        for roletype, params in self.valid_values.items():
            if () == type(list(Role)[0]):
                for value in self.other_values:
                    self.assertFalse(value in params["keys"])


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