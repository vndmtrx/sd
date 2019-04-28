#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://pythonclub.com.br/what-the-flask-pt-1-introducao-ao-desenvolvimento-web-com-python.html
# http://flask.pocoo.org/docs/1.0/patterns/
import os

from sd_app import create_app

cfg = os.path.abspath('config.cfg')

app = create_app(config=cfg)

@app.shell_context_processor
def cria_contexto_shell():
    from sd_app.compartilhado import sqlalchemy as banco
    from sd_app.usuarios.models import Usuario
    
    return {
        'banco': banco,
        'Usuario': Usuario
    }

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
