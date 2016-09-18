init:
	pip install -r requirements.txt

install: init
	sudo cp nepcal_applet.py /usr/local/bin/nepcal_applet
