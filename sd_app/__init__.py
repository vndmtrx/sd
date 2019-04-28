#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

from .compartilhado import banco

def create_app(config=None):
    app = Flask(__name__)
    
    app.config.from_pyfile(config)
    
    from .main import main
    from .usuarios import blueprint as usuarios
    
    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(usuarios, url_prefix='/usuarios')
    
    banco.init_app(app)
    
    return app
