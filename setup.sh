#!/bin/bash
a1=$(pwd)
loc=/bin/python
venv_loc=$a1$loc
python_loc=$(which python)
echo $python_loc
if [ $venv_loc != $python_loc ]
then
	. venv/bin/activate
	export FLASK_APP=testx.py
fi
flask run
