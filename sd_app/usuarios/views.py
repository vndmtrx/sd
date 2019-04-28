#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template

from sd_app.usuarios import blueprint as usuarios
from sd_app.usuarios.models import Usuario

@usuarios.route('/')
def get_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios/lista.html', usuarios=usuarios)
