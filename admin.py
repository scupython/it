# -*- coding: utf-8 -*-
# admin.py by scupython@gmail.com
# Fri Mar  1 11:00:41 2013

from flask.ext.admin.contrib.sqlamodel import ModelView
from flask.ext.admin.contrib.sqlamodel.filters import FilterLike
from models import *
from models.dbase import db_session
from flask.ext.admin import Admin


class RoleTypeView(ModelView):
    can_delete = False
    def __init__(self,session,**kwargs):
        super(RoleTypeView,self).__init__(RoleType,session,**kwargs)

class DevTypeView(ModelView):
    can_delete = False
    list_columns = ('name','price','note','numbers')
    def __init__(self,session,**kwargs):
        super(DevTypeView,self).__init__(DevType,session,**kwargs)
        self._auto_joins=[]
class DepartmentView(ModelView):
    can_delete = False
    list_columns = ('name','belong_to','sub_group','employee_num')
    searchable_columns=('name',)
    def __init__(self,session,**kwargs):
        super(DepartmentView,self).__init__(Department,session,**kwargs)
        self._auto_joins = []
class EmployeeView(ModelView):
    can_delete = False
    list_columns = ('empId','name','department','used_devs')
    searchable_columns = ('name',)
    def __init__(self,session,**kwargs):
        super(EmployeeView,self).__init__(Employee,session,**kwargs)
        self._auto_joins = []
class DevView(ModelView):
    can_delete = False
    searchable_columns = ('lable',)
    list_columns=('lable','used_now_by','detail','note')
    def __init__(self,session,**kwargs):
        super(DevView,self).__init__(Dev,session,**kwargs)
        self._auto_joins = []
#rtadmin = RoleTypeView(db_session,name=u'角色类型')
dtadmin = DevTypeView(db_session,name=u'设备类型')
dpadmin = DepartmentView(db_session,name=u'部门')
empadmin = EmployeeView(db_session,name=u'员工')
devadmin = DevView(db_session,name=u'设备')

admin = Admin()
#admin.add_view(rtadmin)
admin.add_view(dtadmin)
admin.add_view(dpadmin)
admin.add_view(empadmin)
admin.add_view(devadmin)

