#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://pythonclub.com.br/what-the-flask-pt-1-introducao-ao-desenvolvimento-web-com-python.html

from sd_app import create_app

if __name__ == '__main__':
    app = create_app(config='config.py')
    app.run(debug=True, use_reloader=True)
