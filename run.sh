#!/bin/bash

if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
  exit 1
fi


python3 -m venv .venv
source .venv/bin/activate
pip3 install rich
pip3 install emoji
python3 main.py

# chmod +x run.sh
# ./run.sh to run