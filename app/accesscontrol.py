#! /usr/bin/python3
# -*- coding: utf-8 -*-
# app/accesscontrol.py
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
    regular_client = {
        Resource.account_balance : [Access.READ],
        Resource.investment_portfolio : [Access.READ],
        Resource.advisor_contact : [Access.READ]
    }
    premium_client = regular_client.copy()
    premium_client.update({
        Resource.investment_portfolio : [Access.READ, Access.WRITE],
        Resource.planner_contact : [Access.READ], 
        Resource.analyst_contact : [Access.READ]
    })
    teller = {
        Resource.account_balance : [Access.READ 
        if (not ((datetime.now().hour < 8) or (datetime.now().hour > 17))) else None],
        Resource.investment_portfolio : [Access.READ 
        if (not ((datetime.now().hour < 8) or (datetime.now().hour > 17))) else None]
    }
    financial_advisor = {
        Resource.account_balance : [Access.READ],
        Resource.investment_portfolio : [Access.READ, Access.WRITE],
        Resource.consumer_instruments : [Access.READ]
    }
    financial_planner = financial_advisor.copy()
    financial_planner.update({
        Resource.market_instruments : [Access.READ]
    })
    investment_analyst = financial_planner.copy()
    investment_analyst.update({
        Resource.interest_instruments : [Access.READ],
        Resource.derivative_trading : [Access.READ]
    })
    compliance_officer = {
        Resource.account_balance : [Access.READ],
        Resource.investment_portfolio : [Access.READ, Access.OWN]
    }
    technical_support = {
        Resource.client_information : [Access.READ],
        Resource.account_access : None
    }


# Local variables:
# mode: python
# End:
# vim: filetype=python fileencoding=utf-8 :