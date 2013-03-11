# -*- coding: utf-8 -*-
# dev.py scupython@gmail.com
# Thu Feb 28 18:00:23 2013

from dbase import Base
from datetime import datetime
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String,Float, Text,DateTime, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import text

class Dev(Base):
    __tablename__ = 'dev'
    id = Column(Integer,primary_key=True)
    lable = Column(String(63),nullable=False)
    type = Column(Integer,ForeignKey('devtype.id'),nullable=False)
    status = Column(String(32))
    detail = Column(Text)
    note = Column(Text)

    added_at = Column(DateTime,default=datetime.now,nullable=False)
    added_by_id = Column(Integer,ForeignKey('employee.id'),nullable=False)
    deleted_at = Column(DateTime,nullable=True,
                        server_default=text('NULL'))
    deleted_by_id = Column(Integer,ForeignKey('employee.id'),
                           nullable=True,
        server_default=text('NULL'))
    
    deleted = Column(Boolean, default=False)

    used_now_by_id = Column(Integer,ForeignKey('employee.id'),
                         nullable=False)
    
    devtype = relationship('DevType',backref=backref('devs'))
    added_by = relationship('Employee',
                            primaryjoin='Employee.id==Dev.added_by_id')
    delete_by = relationship('Employee',
                             primaryjoin='Employee.id==Dev.deleted_by_id')

    used_now_by = relationship('Employee',
                               primaryjoin='Employee.id==Dev.used_now_by_id',
                               backref=backref('devs'))

    
    def __unicode__(self):
        return u'%s' %self.lable

    def __repr__(self):
        return self.__unicode__()
    
