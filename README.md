# instruction: #

        sh setup.sh  ( to create virtual environment for our packages)

# or do the following: #
        python3 -m venv venv
        . venv/bin/activate
        python3 -m pip install --upgrade pip
        pip3 install -r requirements.txt
        export FLASK_APP=testx.py
        
        flask run
and open 127.0.0.1:5000 on your browser

## works for python3, not python2. ##  
### So if you encounter any import error, you may want to change your default interpreter to python3.###

