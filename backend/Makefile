.PHONY: setup run help

setup: venv

run: venv
	penv/bin/python3 src/main.py;

help:
	echo "setup: creates a virtual environment with the proper python version and dependencies";
	echo "run: runs the python backend app using the virtual enviornment created by `make setup`"

venv: penv/bin/python3 penv/bin/pip3
	
penv/bin/python3:
	virtualenv -p python3 penv;
	penv/bin/pip3 install -r requirements.txt

penv/bin/pip3:
	virtualenv -p python3 penv;
	penv/bin/pip3 install -r requirements.txt
