# instruction: #

        sh setup.sh  ( to create virtual environment for our packages)

# or do the following: #
        python3 -m venv venv
        . venv/bin/activate
        python3 -m pip install --upgrade pip
        pip3 install -r requirements.txt
        export FLASK_APP=testx.py
        
        flask run
        
# for windows users: (assuming that python < 3.6 has already been installed) #
        py -m venv venv
        venv\Scripts\activate.bat
        pip3 install -r requirements.txt
        export FLASK_APP=testx.py
        
        flask run
and open 127.0.0.1:5000 on your browser

## works for python3.6 and before, not python2. ##  
## also somehow python3.7 or above does not support pip install tensorflow ##
### So if you encounter any import error, you may want to change your interpreter to python3.6 and below###

