#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sd_app.compartilhado import sqlalchemy as banco

class Usuario(banco.Model):
    __tablename__ = 'usuarios'
    id = banco.Column(banco.Integer, primary_key=True)
    login = banco.Column(banco.String(20), unique=True, nullable=False)
    nome = banco.Column(banco.String(80), nullable=False)
    email = banco.Column(banco.String(50), unique=True, nullable=False)
    
    def __repr__(self):
        return '<Usuario {0}>'.format(self.usuario)
