#!/bin/bash

rm -Rf dist/
virtualenv env
source env/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
python3 -m build
python3 -m pip install --upgrade twine

# Generate token 
# tr -dc 'A-Za-z0-9' </dev/urandom | head -c 40  ; echo
#python3 -m twine upload dist/*