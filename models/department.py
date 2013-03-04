# -*- coding: utf-8 -*-
# department.py scupython@gmail.com
# Thu Feb 28 18:32:29 2013
from dbase import Base
from sqlalchemy import Column,ForeignKey
from sqlalchemy.types import Integer,String
from sqlalchemy.orm import relationship,backref
class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    pid = Column(Integer,ForeignKey('department.id'))
    #groups = relationship("Department")
    groups = relationship("Department",
            backref=backref('belong_to',remote_side=[id]))
    def __unicode__(self):
        return u'%s' %self.name

    def __repr__(self):
        return self.__unicode__()
