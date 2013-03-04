# -*- coding: utf-8 -*-
# devtype.py scupython@gmail.com
# Thu Feb 28 17:40:17 2013

from dbase import Base
from sqlalchemy import Column
from sqlalchemy.types import Integer,String,Text,Float
from sqlalchemy.ext.hybrid import hybrid_property

class DevType(Base):
    __tablename__ = 'devtype'
    id = Column(Integer,primary_key=True)
    name = Column(String(63),nullable=False)
    price = Column(Float,nullable=False,default=0.0)
    note = Column(Text)

    @hybrid_property
    def numbers(self):
        devs = [u'%s' %d.lable for d in self.devs]
        return 'total %d ' % len(devs)
    def __unicode__(self):
        return u'%s' %self.name

    def __repr__(self):
        return self.__unicode__()
        
