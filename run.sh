#!/bin/bash


# check if python is installed
command -v python3 >/dev/null 2>&1 && echo Python 3 is installed  # POSIX-compliant
type -P python3 >/dev/null 2>&1 && echo Python 3 is installed     # Bash only
# check if venv exists


python3 -m venv .venv
source .venv/bin/activate
pip3 install rich
pip3 install emoji
python3 main.py

# chmod +x run.sh
# ./run.sh to run