#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sd_app.compartilhado import sqlalchemy as banco
from sqlalchemy.ext.hybrid import hybrid_property
from passlib.hash import sha256_crypt

class Usuario(banco.Model):
    __tablename__ = 'usuarios'
    id = banco.Column(banco.Integer, primary_key=True)
    login = banco.Column(banco.String(20), unique=True, index=True, nullable=False)
    email = banco.Column(banco.String(50), unique=True, index=True, nullable=False)
    nome = banco.Column(banco.String(150), nullable=False)
    _senha = banco.Column(banco.String(80), nullable=False)
    
    @hybrid_property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha):
        self._senha = sha256_crypt.hash(senha)
    
    def __repr__(self):
        return '<Usuario {0}>'.format(self.login)
