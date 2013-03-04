# -*- coding: utf-8 -*-
# roletype.py scupython@gmail.com
# Fri Mar  1 09:30:11 2013

from dbase import Base
from sqlalchemy import Column
from sqlalchemy.types import Integer,String

class RoleType(Base):
    __tablename__ = 'roletype'
    id = Column(Integer, primary_key=True)
    name = Column(String(32),nullable=False)

    def __unicode__(self):
        return u'%s' %self.name

    def __repr__(self):
        return self.__unicode__()
