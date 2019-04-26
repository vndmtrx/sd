#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

from .main import main
from .admin import admin

def create_app(config=None):
    app = Flask(__name__)
    if config:
        app.config.from_pyfile(config)
    
    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/admin')
    
    return app
