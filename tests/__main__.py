#! /usr/bin/python3
# -*- coding: utf-8 -*-
# tests/__main__.py
# Part of test, a package providing testing access control mechanism.
#
# Copyright © 2023 trong0dn


#  ----------------- Unit test framework
import unittest

#  ----------------  Individual test suites
from tests.test_accesscontrol import suite_accesscontrol
from tests.test_enrolment import suite_enrolment
from tests.test_pwdfile import suite_pwdfile
from tests.test_login import suite_login


def __main__(argv=None):
    """ Mainline function for this module. """
    import sys as _sys
    if not argv:
        argv = _sys.argv
    exitcode = None
    try:
        unittest.main(argv=argv)
    except SystemExit as exc:
        exitcode = exc.code
    return exitcode


if __name__ == '__main__':
    import sys
    exitcode = __main__(sys.argv)
    sys.exit(exitcode)


# Local variables:
# mode: python
# End:
# vim: filetype=python fileencoding=utf-8 :