#!/bin/bash
cd ~/guia
sudo snap install -y pycharm-community --classic
sudo apt install -y python3-pip
sudo apt-get install -y python3-venv
mkdir capitulo_3
cd capitulo_3
python3 -m venv virtual_enviroment_1
source virtual_enviroment_1/bin/activate
sudo apt update
sudo apt install -y libpq-dev postgresql postgresql-contrib
pip3 install django
pip3 install psycopg2

django-admin.py startproject cap3_project .

python3 manage.py startapp cap3_app

pycharm-community & ~/guia/

python3 manage.py runserver
