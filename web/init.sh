sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/gunicorn restart
