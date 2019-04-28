#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template

from . import users

@users.route('/')
def get_users():
    return render_template('users.html')
