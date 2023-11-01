### The access control mechanism
import enum
from datetime import datetime


class Access(enum.Enum):
    """Describes the way in which a role (subject) may access an object."""
    READ = enum.auto()
    WRITE = enum.auto()
    OWN = enum.auto()


class Object(enum.Enum):
    """Describes the resources to which access is controlled."""
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
    """Describes the entities capable of accessing objects."""
    regular_client = {
        Object.account_balance : [Access.READ],
        Object.investment_portfolio : [Access.READ],
        Object.advisor_contact : [Access.READ]
    }
    premium_client = {
        Object.account_balance : [Access.READ],
        Object.investment_portfolio : [Access.READ, Access.WRITE],
        Object.planner_contact : [Access.READ], 
        Object.analyst_contact : [Access.READ]
    }
    teller = {
        Object.account_balance : [Access.READ 
        if (not (datetime.now().hour < 8) or (datetime.now().hour > 17)) else None],
        Object.investment_portfolio : [Access.READ 
        if (not (datetime.now().hour < 8) or (datetime.now().hour > 17)) else None]
    }
    financial_advisor = {
        Object.account_balance : [Access.READ],
        Object.investment_portfolio : [Access.READ, Access.WRITE],
        Object.consumer_instruments : [Access.READ]
    }
    financial_planner = financial_advisor.copy()
    financial_planner.update({
        Object.market_instruments : [Access.READ]
    })
    investment_analyst = financial_planner.copy()
    investment_analyst.update({
        Object.interest_instruments : [Access.READ],
        Object.derivative_trading : [Access.READ]
    })
    compliance_officer = {
        Object.account_balance : [Access.READ],
        Object.investment_portfolio : [Access.READ, Access.OWN]
    }
    technical_support = {
        Object.client_information : [Access.READ],
        Object.account_access : None
    }


if __name__ == '__main__':
    print(Access.__members__)
    print(Object.__members__)
    print(Role.__members__)
