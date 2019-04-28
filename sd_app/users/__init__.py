#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

users = Blueprint('users', __name__, template_folder='templates')

from . import views
