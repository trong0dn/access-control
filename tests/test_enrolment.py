#! /usr/bin/python3
# -*- coding: utf-8 -*-
# tests/test_enrolment.py
# Part of test, a package providing testing enrolment mechanism and the proactive password checker.
#
# Copyright © 2023 trong0dn

""" Unit test for 'enrolment' module.
    """

import os
import unittest
import app.enrolment as enrolment


BLOCKLIST = "etc/blocklist.txt"


def setup_fixtures(testcase):
    """ Set up fixtures for test cases using 'enrolment'. """
    testcase.testname = "testname"
    testcase.len7 = "TwG4v$i"
    testcase.len8 = "TwG4v$iL"
    testcase.len9 = "TwG4v$iLf"
    testcase.len10 = "TwG4v$iLf8"
    testcase.len11 = "TwG4v$iLf8%"
    testcase.len12 = "TwG4v$iLf8%p"
    testcase.len13 = "TwG4v$iLf8%pr"
    testcase.noupper = "twg4v$ilf8%p"
    testcase.withupper = "Twg4v$ilf8%p"
    testcase.nolower = "TWG4V$ILF8%P"
    testcase.withlower = "tWG4V$ILF8%P"
    testcase.nodigit = "TwGXv$iLfX%p"
    testcase.withdigit = "TwG4v$iLfX%p"
    testcase.nospecialchar = "TwG4vSiLf8Xp"
    testcase.withspecialchar = "TwG4v$iLf8Xp"
    testcase.weakpwd1 = "Password1"
    testcase.weakpwd2 = "Qwerty123"
    testcase.weakpwd3 = "Qaz123wsx"
    testcase.newweakpwd = "Yi?@wQa07U"
    testcase.calendar = "2023-12-04"
    testcase.license = "CAJA723"
    testcase.telephone = "613-520-2600"
    testcase.numbers = "1234567890"
    testcase.okpwd1 = "h$fy5%4Pm5"
    testcase.okpwd2 = "rJ@!7fhG?3"
    testcase.okpwd3 = "*LRio&5D7#"


class Test_Enrolment(unittest.TestCase):
    """ Test case for the enrolment module. """

    def setUp(self):
        """ Set up the test fixtures. """
        setup_fixtures(self)

    def test_password_policy_length_less_than_eight(self):
        """ Password less than 8 characters in length. """
        self.assertFalse(enrolment.password_policy(self.testname, self.len7))

    def test_password_policy_length_eight(self):
        """ Password 8 characters in length. """
        self.assertTrue(enrolment.password_policy(self.testname, self.len8))

    def test_password_policy_length_nine(self):
        """ Password 9 characters in length. """
        self.assertTrue(enrolment.password_policy(self.testname, self.len9))

    def test_password_policy_length_ten(self):
        """ Password 10 characters in length. """
        self.assertTrue(enrolment.password_policy(self.testname, self.len10))

    def test_password_policy_length_eleven(self):
        """ Password 11 characters in length. """
        self.assertTrue(enrolment.password_policy(self.testname, self.len11))

    def test_password_policy_length_twelve(self):
        """ Password 12 characters in length. """
        self.assertTrue(enrolment.password_policy(self.testname, self.len12))

    def test_password_policy_length_more_than_twelve(self):
        """ Password more than 12 characters in length. """
        self.assertFalse(enrolment.password_policy(self.testname, self.len13))

    def test_password_policy_no_uppercase(self):
        """ Password with no upper-case letter. """
        self.assertFalse(enrolment.password_policy(self.testname, self.noupper))

    def test_password_policy_with_uppercase(self):
        """ Password with an upper-case letter. """
        self.assertTrue(enrolment.password_policy(self.testname, self.withupper))

    def test_password_policy_no_lowercase(self):
        """ Password with no lower-case letter. """
        self.assertFalse(enrolment.password_policy(self.testname, self.nolower))

    def test_password_policy_with_lowercase(self):
        """ Password with a lower-case letter. """
        self.assertTrue(enrolment.password_policy(self.testname, self.withlower))

    def test_password_policy_no_digit(self):
        """ Password with no digits. """
        self.assertFalse(enrolment.password_policy(self.testname, self.nodigit))

    def test_password_policy_with_digit(self):
        """ Password with a digit. """
        self.assertTrue(enrolment.password_policy(self.testname, self.withdigit))

    def test_password_policy_no_special_character(self):
        """ Password with no special character. """
        self.assertFalse(enrolment.password_policy(self.testname, self.nospecialchar))

    def test_password_policy_with_special_character(self):
        """ Password with a special character. """
        self.assertTrue(enrolment.password_policy(self.testname, self.withspecialchar))

    def test_password_policy_with_weak_password1(self):
        """ Password is a 'Password1' weak password. """
        self.assertFalse(enrolment.password_policy(self.testname, self.weakpwd1))

    def test_password_policy_with_weak_password2(self):
        """ Password is a 'Qwerty123' weak password. """
        self.assertFalse(enrolment.password_policy(self.testname, self.weakpwd2))

    def test_password_policy_with_weak_password3(self):
        """ Password is a 'Qaz123wsx' weak password. """
        self.assertFalse(enrolment.password_policy(self.testname, self.weakpwd3))

    def test_password_policy_with_newly_added_weak_password(self):
        """ Password is a newly added weak password. """
        self.assertTrue(enrolment.password_policy(self.testname, self.newweakpwd))
        enrolment.add_disallowed_password(self.newweakpwd)
        self.assertFalse(enrolment.password_policy(self.testname, self.newweakpwd))

    def test_password_policy_match_calendar_date(self):
        """ Password is matching calendar date format. """
        self.assertFalse(enrolment.password_policy(self.testname, self.calendar))

    def test_password_policy_match_license_plate(self):
        """ Password is matching license plate format. """
        self.assertFalse(enrolment.password_policy(self.testname, self.license))

    def test_password_policy_match_telephone_number(self):
        """ Password is matching telephone number format. """
        self.assertFalse(enrolment.password_policy(self.testname, self.telephone))

    def test_password_policy_match_number_only(self):
        """ Password is matching common number format. """
        self.assertFalse(enrolment.password_policy(self.testname, self.numbers))

    def test_password_policy_match_userId(self):
        """ Password is matching user id. """
        self.assertFalse(enrolment.password_policy(self.testname, self.testname))

    def test_password_policy_ok_pasword1(self):
        """ Password is valid to the policy. """
        self.assertTrue(enrolment.password_policy(self.testname, self.okpwd1))

    def test_password_policy_ok_pasword1(self):
        """ Password is valid to the policy. """
        self.assertTrue(enrolment.password_policy(self.testname, self.okpwd2))

    def test_password_policy_ok_pasword1(self):
        """ Password is valid to the policy. """
        self.assertTrue(enrolment.password_policy(self.testname, self.okpwd3))

    def tearDown(self):
        """ Tear down and clean added blocked passwords list. """
        with open(BLOCKLIST, 'r') as file:
            lines = file.readlines()
        with open(BLOCKLIST, 'w') as file:
            for line in lines:
                if line.strip("\n") != self.newweakpwd:
                    file.write(line)


def suite_enrolment():
    """ Create the test suite for this module. """
    from sys import modules
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(modules[__name__])
    return suite


# Local variables:
# mode: python
# End:
# vim: filetype=python fileencoding=utf-8 :