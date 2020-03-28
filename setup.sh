#!/bin/bash
a1=$(pwd)
loc=/bin/python
venv_loc=$a1$loc
python_loc=$(which python)
echo $venv_loc
echo $python_loc
PYTHONPATH=venv/lib/python3.6/site-packages:$PYTHONPATH
PYTHONPATH=venv/bin:$PYTHONPATH
export PYTHONPATH
if [ $venv_loc != $python_loc ]
then
	. venv/bin/activate
	export FLASK_APP=testx.py
fi
flask run
