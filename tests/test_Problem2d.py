#! /usr/bin/python3
# -*- coding: utf-8 -*-
# tests/test_Problem2d.py
# Part of test, a package providing testing password file mechanism.
#
# Copyright © 2023 trong0dn

""" Unit test for 'login' module.
    """

import unittest
import app.Problem2c as pwdfile


DATABASE = "etc/passwd.txt"


def setup_fixtures(testcase):
    """ Set up fixtures for test cases using 'pwdfile'. """
    testcase.testname = "username"
    testcase.nonename = "doesnotexist"
    testcase.password = "TwG4v$iLf8%p"
    testcase.role_not_exist = "test_role"
    testcase.premium_client = "premium_client"

    testcase.regular_client = 'regular_client'
    testcase.premium_client = 'premium_client'
    testcase.teller = 'teller'
    testcase.financial_advisor = 'financial_advisor'
    testcase.financial_planner = 'financial_planner'
    testcase.investment_analyst = 'investment_analyst'
    testcase.compliance_officer = 'compliance_officer'
    testcase.technical_support = 'technical_support'

    testcase.regular_client1 = "mischa.lowery"
    testcase.regular_client2 ="veronica.perez"
    testcase.regular_client_fullname1 = "Mischa Lowery"
    testcase.regular_client_fullname2 = "Veronica Perez"

    testcase.premium_client1 = "willow.garza"
    testcase.premium_client2 = "nala.preston"
    testcase.premium_client_fullname1 = "Willow Garza"
    testcase.premium_client_fullname2 = "Nala Preston"

    testcase.teller1 = "winston.callahan"
    testcase.teller2 = "kelan.gough"
    testcase.teller_fullname1 = "Winston Callahan"
    testcase.teller_fullname2 = "Kelan Gugh"

    testcase.financial_advisor1 = "nelson.wilkins"
    testcase.financial_advisor2 = "kelsi.chang"
    testcase.financial_advisor_fullname1 = "Nelson Wilkins"
    testcase.financial_advisor_fullname2 = "Kelsi Chang"

    testcase.financial_planner1 = "kodi.matthews"
    testcase.financial_planner2 = "malikah.wu"
    testcase.financial_planner_fullname1 = "Kodi Matthews"
    testcase.financial_planner_fullname2 = "Malikah Wu"

    testcase.investment_analyst1 = "stacy.kent"
    testcase.investment_analyst2 = "keikilana.kapahu"
    testcase.investment_analyst_fullname1 = "Stacy Kent"
    testcase.investment_analyst_fullname2 = "Keikilana Kapahu"
    
    testcase.compliance_officer1 = "howard.linkler"
    testcase.compliance_officer2 = "stefania.smart"
    testcase.compliance_officer_fullname1 = "Howard Linkler"
    testcase.compliance_officer_fullname2 = "Stefania Smart"

    testcase.technical_support1 = "caroline.lopez"
    testcase.technical_support2 = "pawel.barclay"
    testcase.technical_support_fullname1 = "Caroline Lopez"
    testcase.technical_support_fullname2 = "Pawel Barclay"

    
class Test_Pwdfile(unittest.TestCase):
    """ Test case for the pwdfile module. """

    def setUp(self):
        """ Set up the test fixtures. """
        setup_fixtures(self)

    def test_create_record(self):
        """ Able to create a record with valid username and password. """
        self.assertTrue(pwdfile.create_record(self.testname, self.password, self.premium_client, self.premium_client))

    def test_create_record_duplicate(self):
        """ Unable to create a record with username existing in the system. """
        pwdfile.create_record(self.testname, self.password, self.premium_client, self.testname)
        self.assertFalse(pwdfile.create_record(self.testname, self.password, self.premium_client, self.premium_client))

    def test_create_record_with_invalid_role(self):
        """ Unable to create a record with invalid role. """
        self.assertFalse(pwdfile.create_record(self.testname, self.password, self.role_not_exist, self.role_not_exist))

    def test_retrive_record(self):
        """ Able to retrieve a record with username existing in the system. """
        pwdfile.create_record(self.testname, self.password, self.premium_client, self.testname)
        self.assertEqual(pwdfile.retrieve_record(self.testname, self.password), 2)

    def test_retrive_record_not_exist(self):
        """ Able to retrieve a record with username not existing in the system. """
        self.assertIsNone(pwdfile.retrieve_record(self.nonename, self.password))

    def test_verify_crediential(self):
        """ Able to retrieve a record with username existing in the system. """
        pwdfile.create_record(self.testname, self.password, self.premium_client, self.testname)
        self.assertTrue(pwdfile.verify_credential(self.testname, self.password))

    def test_verify_crediential_not_exist(self):
        """ Able to retrieve a record with username existing in the system. """
        self.assertFalse(pwdfile.verify_credential(self.nonename, self.password))

    def test_add_regular_client(self):
        """ Add regular client record. """
        self.assertTrue(pwdfile.create_record(self.regular_client1, self.password, self.regular_client, self.regular_client_fullname1))
        self.assertTrue(pwdfile.create_record(self.regular_client2, self.password, self.regular_client, self.regular_client_fullname2))

    def test_add_premium_client(self):
        """ Add premium client record. """
        self.assertTrue(pwdfile.create_record(self.premium_client1, self.password, self.premium_client, self.premium_client_fullname1))
        self.assertTrue(pwdfile.create_record(self.premium_client2, self.password, self.premium_client, self.premium_client_fullname2))

    def test_add_teller(self):
        """ Add premium client record. """
        self.assertTrue(pwdfile.create_record(self.teller1, self.password, self.teller, self.teller_fullname1))
        self.assertTrue(pwdfile.create_record(self.teller2, self.password, self.teller, self.teller_fullname2))

    def test_add_financial_advisor(self):
        """ Add financial advisor record. """
        self.assertTrue(pwdfile.create_record(self.financial_advisor1, self.password, self.financial_advisor, self.financial_advisor_fullname1))
        self.assertTrue(pwdfile.create_record(self.financial_advisor2, self.password, self.financial_advisor, self.financial_advisor_fullname2))

    def test_add_financial_planner(self):
        """ Add financialplanner record. """
        self.assertTrue(pwdfile.create_record(self.financial_planner1, self.password, self.financial_planner, self.financial_planner_fullname1))
        self.assertTrue(pwdfile.create_record(self.financial_planner2, self.password, self.financial_planner, self.financial_planner_fullname2))

    def test_add_investment_analyst(self):
        """ Add investment_analyst record. """
        self.assertTrue(pwdfile.create_record(self.investment_analyst1, self.password, self.investment_analyst, self.investment_analyst_fullname1))
        self.assertTrue(pwdfile.create_record(self.investment_analyst2, self.password, self.investment_analyst, self.investment_analyst_fullname2))

    def test_add_compliance_officer(self):
        """ Add compliance officer record. """
        self.assertTrue(pwdfile.create_record(self.compliance_officer1, self.password, self.compliance_officer, self.compliance_officer_fullname1))
        self.assertTrue(pwdfile.create_record(self.compliance_officer2, self.password, self.compliance_officer, self.compliance_officer_fullname2))

    def test_add_technical_support(self):
        """ Add technical support record. """
        self.assertTrue(pwdfile.create_record(self.technical_support1, self.password, self.technical_support, self.technical_support_fullname1))
        self.assertTrue(pwdfile.create_record(self.technical_support2, self.password, self.technical_support, self.technical_support_fullname2))

    def tearDown(self):
        """ Tear down and clean added password in passwords list. """
        with open(DATABASE, 'r') as file:
            lines = file.readlines()
        with open(DATABASE, 'w') as file:
            for line in lines:
                if line.find(self.testname):
                    line.strip("\n")
                    file.write(line)
        file.close()

    
def suite_pwdfile():
    """ Create the test suite for this module. """
    from sys import modules
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(modules[__name__])
    return suite


# Local variables:
# mode: python
# End:
# vim: filetype=python fileencoding=utf-8 :