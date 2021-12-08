#!/bin/bash
curDir=$(pwd)

	
	sudo ln -sf /home/box/web/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
	sudo rm -rf /home/box/web/web/etc/nginx/sites-enabled/default
	sudo /etc/init.d/nginx restart

	sudo ln -sf /home/box/web/web/etc/gunicorn.conf   /etc/gunicorn.d/test
	sudo /home/box/web/web/etc/init.d/gunicorn restart

	cd /home/box/web/web/ask/ask
	gunicorn -b 127.0.0.1:8000 wsgi



