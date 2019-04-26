#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template

from . import admin

@admin.route('/')
def get_admin():
    return render_template('admin.html')
