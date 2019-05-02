#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

blueprint = Blueprint('usuarios', __name__, template_folder='templates')

from . import views
