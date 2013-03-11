# -*- coding: utf-8 -*-
# dbase.py scupython@gmail.com 
# Thu Feb 28 17:30:55 2013

SQLALCHEMY_DATABASE_URI='mysql://elexit:dM#nh^qVeQu^Pk7Bx@localhost/elex_it?charset=utf8'

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

elex_it_engine = create_engine(SQLALCHEMY_DATABASE_URI,encoding='utf-8',pool_recycle=3600)
Session = scoped_session(sessionmaker(bind=elex_it_engine,autocommit=False))

db_session = Session()
metadata = MetaData()
Base = declarative_base(metadata=metadata)
