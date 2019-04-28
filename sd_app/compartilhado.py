#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

sqlalchemy = SQLAlchemy()

migrate = Migrate()
