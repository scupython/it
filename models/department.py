# -*- coding: utf-8 -*-
# department.py scupython@gmail.com
# Thu Feb 28 18:32:29 2013
from dbase import Base
from sqlalchemy import Column,ForeignKey
from sqlalchemy.types import Integer,String
from sqlalchemy.orm import relationship,backref
from sqlalchemy.ext.hybrid import hybrid_property
class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    pid = Column(Integer,ForeignKey('department.id'))
    #groups = relationship("Department")
    groups = relationship("Department",
            backref=backref('belong_to',remote_side=[id]))
    def __unicode__(self):
        if self.belong_to:
            return u'%s--%s' %(self.belong_to,self.name)
        return u'%s' %self.name

    def __repr__(self):
        return self.__unicode__()

    @hybrid_property
    def sub_group(self):
        return ','.join([d.name for d in self.groups])
