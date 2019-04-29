#!/usr/bin/env bash
## https://exploreflask.com

#Python 3
sudo yum groupinstall "Development Tools"
sudo apt install python36 python36-devel python36-pip openldap-devel
python36 -m venv venv/

source venv/bin/activate
python --version
pip --version

pip install --upgrade pip

pip install wheel

#Dependências da biblioteca Psycopg2
sudo yum install postgresql-devel

pip install -r requirements.txt
#pip install Flask Flask-Login Flask-WTF Flask-SQLAlchemy Flask-Migrate psycopg2

deactivate
