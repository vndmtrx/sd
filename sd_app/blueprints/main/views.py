#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, flash

from . import blueprint as main

@main.route('/')
def get_main():
    flash('Mensagem 1', 'success')
    flash('Mensagem Info', 'info')
    flash('Mensagem Warning', 'warning')
    flash('Mensagem Error', 'danger')
    return render_template('main.html')

@main.route('/teste')
def get_teste():
    return render_template('teste.html')
