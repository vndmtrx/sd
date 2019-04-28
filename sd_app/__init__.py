#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

def create_app(config=None):
    app = Flask(__name__)
    
    app.config.from_pyfile(config)
    
    from .main import main
    from .admin import admin
    from .users import users
    
    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(users, url_prefix='/users')
    
    from .users.models import db as users_db
    
    users_db.init_app(app)
    
    return app
