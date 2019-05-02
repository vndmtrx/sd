#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

class RegistroUsuarioForm(FlaskForm):
    login = StringField('Usuário', [
        validators.InputRequired(),
        validators.Length(min=6, max=20),
        validators.Regexp('^[A-Za-z0-9_.]*$', 0, 'Somente letras, números, underscores e pontos')
        ])
    nome = StringField('Nome', [
        validators.InputRequired(),
        validators.Length(max=80)
        ])
    email = StringField('Email', [
        validators.InputRequired(),
        validators.Length(max=50),
        validators.Email("Formato de e-mail inválido")
        ])
    enviar = SubmitField('Enviar')
