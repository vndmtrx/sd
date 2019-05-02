#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

blueprint = Blueprint('main', __name__, template_folder='templates')

from . import views
