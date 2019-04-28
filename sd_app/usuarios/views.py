#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template

from . import blueprint as usuarios

@usuarios.route('/')
def get_usuarios():
    return render_template('usuarios/lista.html')
