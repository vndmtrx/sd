#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template
from flask_login import login_required

from . import main

@main.route('/')
def get_main():
    return render_template('main.html')

@main.route('teste')
@login_required
def get_teste():
    return render_template('teste.html')
