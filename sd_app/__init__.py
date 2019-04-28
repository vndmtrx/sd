#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

def create_app(config=None):
    app = Flask(__name__, instance_relative_config=False)
    
    app.config.from_pyfile(config)
    
    from sd_app.main import main
    from sd_app.usuarios import blueprint as usuarios
    
    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(usuarios, url_prefix='/usuarios')
    
    from sd_app.compartilhado import sqlalchemy as banco
    banco.init_app(app)
    
    return app
