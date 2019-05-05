#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import IntegerField, HiddenField, StringField, SubmitField, validators
from wtforms.validators import ValidationError

from .models import Usuario

class RegistroUsuarioForm(FlaskForm):
    id = HiddenField('Id')
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
    
    def validate_login(self, field):
        usr = Usuario.query.filter_by(login=field.data).first()
        if usr and str(usr.id) != self.id.data:
            raise ValidationError('Usuário {} já está em uso!'.format(field.data))
    
    def validate_email(self, field):
        usr = Usuario.query.filter_by(email=field.data).first()
        if usr and str(usr.id) != self.id.data:
            raise ValidationError('E-mail {} já está em uso!'.format(field.data))
