# -*- coding: utf-8 -*-

from dbase import elex_it_engine
from roletype import RoleType
from department import Department
from devtype import DevType
from employee import Employee
from dev import Dev


def creatable():
    RoleType.__table__.create(elex_it_engine)
    Department.__table__.create(elex_it_engine)
    DevType.__table__.create(elex_it_engine)
    Employee.__table__.create(elex_it_engine)
    Dev.__table__.create(elex_it_engine)
