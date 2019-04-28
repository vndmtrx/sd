#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template

from . import main

@main.route('/')
def get_main():
    return render_template('main.html')

@main.route('/teste')
def get_teste():
    return render_template('teste.html')
