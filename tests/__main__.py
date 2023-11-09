#! /usr/bin/python3
# -*- coding: utf-8 -*-
# tests/__main__.py
# Part of test, a package providing testing access control mechanism.
#
# Copyright © 2023 trong0dn


import unittest

from tests.test_Problem1e import suite_accesscontrol
from tests.test_Problem2d import suite_enrolment
from tests.test_Problem3d import suite_pwdfile
from tests.test_Problem4d import suite_login


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