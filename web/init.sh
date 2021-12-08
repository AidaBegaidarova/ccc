#!/bin/bash
curDir=$(pwd)

	
	sudo ln -sf ~/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
	sudo rm -rf /etc/nginx/sites-enabled/default
	sudo /etc/init.d/nginx restart

	sudo ln -sf ~/web/etc/gunicorn.conf   /etc/gunicorn.d/test
	sudo /etc/init.d/gunicorn restart

	cd ~/web/ask/ask
	gunicorn -b 127.0.0.1:8000 wsgi



