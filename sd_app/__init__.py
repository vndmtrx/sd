#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_login import LoginManager

from .main import main
from .admin import admin

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
