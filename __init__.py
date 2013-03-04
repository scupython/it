# -*- coding: utf-8 -*-
# 
from flask import Flask

app = Flask(__name__)
app.config['CSRF_ENABLED'] = False
app.config['SECRET_KEY']= '\x1b\xf6UX\xc8\xd3\x99W3\xb4\xb7z\xd4\xa5\x88\xad\xf4%\x81\x9d\xde\xd2h\x8c'

from models.dbase  import db_session
@app.after_request
def shutdown_session(response):
    db_session.close()
    return response

from admin import admin
admin.init_app(app)
