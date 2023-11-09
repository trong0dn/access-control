#! /usr/bin/python3
# -*- coding: utf-8 -*-
# src/__main__.py
# Part of src, a package providing access control mechanism.
#
# Copyright © 2023 trong0dn

import app.Problem4c as login


def __main__(argv=None):
    """ Mainline function for this module. """
    import sys as _sys
    if not argv:
        argv = _sys.argv
    exitcode = None
    try:
        login.user_interface()
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