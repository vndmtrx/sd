#!/usr/bin/env bash
## https://exploreflask.com

#Python 3
sudo apt install python3-pip python3-venv
python3 -m venv venv/

source venv/bin/activate
python --version
pip --version

pip install --upgrade pip

pip install wheel

#Dependências das bibliotecas LDAP, SQLAlchemy e Psycopg2
sudo apt install build-essential python3-dev libsasl2-dev libldap2-dev libssl-dev libpq-dev

pip install -r requirements.txt
deactivate
