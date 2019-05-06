#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, request, flash, redirect, url_for, abort

from sd_app.compartilhado import sqlalchemy as banco

from . import blueprint as usuarios
from .models import Usuario
from .forms import RegistroUsuarioForm

@usuarios.route('/')
def get_usuarios():
    usrs = Usuario.query.all()
    return render_template('usuarios/lista.html', usuarios=usrs)

@usuarios.route('/<string:login>')
def get_usuario(login):
    usr = Usuario.query.filter_by(login=login).first()
    return render_template('usuarios/item.html', usuario=usr)

@usuarios.route('/adicionar', methods=['GET', 'POST'])
def adicionar_usuario():
    form = RegistroUsuarioForm(request.form)
    if form.validate_on_submit():
        usr = Usuario(
            login=form.login.data,
            email=form.email.data,
            nome=form.nome.data
        )
        usr.senha = form.senha.data
        banco.session.add(usr)
        banco.session.commit()
        flash('Cadastrado com sucesso', 'success')
        return redirect(url_for('.get_usuario', login=usr.login))
    return render_template('usuarios/registro.html', form=form)

@usuarios.route('/<string:login>/editar', methods=['GET', 'POST'])
def editar_usuario(login):
    usr = Usuario.query.filter_by(login=login).first()
    if usr is not None:
        form = RegistroUsuarioForm(request.form, obj=usr)
        if form.validate_on_submit():
            if form.id.data != str(usr.id):
                abort(403)
            usr.login = form.login.data
            usr.email = form.email.data
            usr.nome = form.nome.data
            if form.senha.data != usr.senha:
                usr.senha = form.senha.data
            banco.session.commit()
            flash('Alterado com sucesso', 'success')
            return redirect(url_for('.get_usuario', login=usr.login))
        return render_template('usuarios/registro.html', form=form)
    else:
        return redirect(url_for('.adicionar_usuario'))
