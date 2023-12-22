#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install rich
pip3 install emoji
echo $VIRTUAL_ENV


if [[ -x "$(command -v python3)" ]]
then
    pyv="$(python -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        python main.py
    else
        echo "Update your version of python!" >&2
    fi 
else
    echo "Python is not installed. To install Python, check out https://installpython3.com/" >&2
fi