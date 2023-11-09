#! /usr/bin/python3
# -*- coding: utf-8 -*-
# app/Problem1d.py
# Part of app, a package providing access control mechanism.
#
# Copyright © 2023 trong0dn

import enum
from datetime import datetime


class Access(enum.Enum):
    """Describes the way in which a Role may access a Resource."""
    READ = enum.auto()
    WRITE = enum.auto()
    OWN = enum.auto()


class Resource(enum.Enum):
    """Describes the objects to which access is controlled."""
    account_balance = enum.auto()
    investment_portfolio = enum.auto()
    advisor_contact = enum.auto()
    planner_contact = enum.auto()
    analyst_contact = enum.auto()
    consumer_instruments = enum.auto()
    market_instruments = enum.auto()
    interest_instruments = enum.auto()
    derivative_trading = enum.auto()
    client_information = enum.auto()
    account_access = enum.auto()


class Role(enum.Enum):
    """Describes the entities capable of accessing Resources."""
    regular_client = enum.auto()
    premium_client = enum.auto()
    teller = enum.auto()
    financial_advisor = enum.auto()
    financial_planner = enum.auto()
    investment_analyst = enum.auto()
    compliance_officer = enum.auto()
    technical_support = enum.auto()


capabilities = {
    Role.regular_client : {
        Resource.account_balance : [Access.READ],
        Resource.investment_portfolio : [Access.READ],
        Resource.advisor_contact : [Access.READ]
    },
    Role.premium_client : {
        Resource.account_balance : [Access.READ],
        Resource.investment_portfolio : [Access.READ, Access.WRITE],
        Resource.advisor_contact : [Access.READ],
        Resource.planner_contact : [Access.READ], 
        Resource.analyst_contact : [Access.READ]
    },
    Role.teller : {
        Resource.account_balance : [Access.READ 
        if (not ((datetime.now().hour < 8) or (datetime.now().hour > 17))) else None],
        Resource.investment_portfolio : [Access.READ 
        if (not ((datetime.now().hour < 8) or (datetime.now().hour > 17))) else None]
    },
    Role.financial_advisor : {
        Resource.account_balance : [Access.READ],
        Resource.investment_portfolio : [Access.READ, Access.WRITE],
        Resource.consumer_instruments : [Access.READ]
    },
    Role.financial_planner : {
        Resource.account_balance : [Access.READ],
        Resource.investment_portfolio : [Access.READ, Access.WRITE],
        Resource.consumer_instruments : [Access.READ],
        Resource.market_instruments : [Access.READ]
    },
    Role.investment_analyst : {
        Resource.account_balance : [Access.READ],
        Resource.investment_portfolio : [Access.READ, Access.WRITE],
        Resource.consumer_instruments : [Access.READ],
        Resource.market_instruments : [Access.READ],
        Resource.interest_instruments : [Access.READ],
        Resource.derivative_trading : [Access.READ]
    },
    Role.compliance_officer : {
        Resource.account_balance : [Access.READ],
        Resource.investment_portfolio : [Access.READ, Access.OWN]
    },
    Role.technical_support : {
        Resource.client_information : [Access.READ],
        Resource.account_access : None
    }
}


# Local variables:
# mode: python
# End:
# vim: filetype=python fileencoding=utf-8 :