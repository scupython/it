# -*- coding: utf-8 -*-
# employee.py scupython@gmail.com
# Fri Mar  1 09:24:44 2013

from dbase import Base
from sqlalchemy import Column,ForeignKey
from sqlalchemy.types import Integer,String
from sqlalchemy.orm import relationship,backref
from sqlalchemy.ext.hybrid import hybrid_property
class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    empId = Column(Integer(11))
    department_id = Column(Integer,ForeignKey('department.id'),nullable=False)
    role_id = Column(Integer,ForeignKey('roletype.id'),nullable=False)
    status = Column(String(16))

    department = relationship('Department',backref=backref('employees',
                                                           lazy='dynamic'))
    role = relationship('RoleType',backref=backref('members',
                                                   lazy='dynamic'))
                
    @hybrid_property
    def used_devs(self):
        devs = [u'%s' %d.lable for d in self.devs]
        return ','.join(devs) + '. total %d ' % len(devs)

    def __unicode__(self):
        return u'%s' %(self.name)

    def __repr__(self):
        return self.__unicode__()



