#!/bin/bash
python3 -m venv venv
. venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
export FLASK_APP=testx.py
flask run

