#!/bin/bash
echo "Creating DB if not exists..."
mysql -u root -e "create database if not exists askpupkin_db;"
mysql -u root -e "grant all on askpupkin_db.* to 'user'@'localhost' identified by 'q1';"
mysql -u user -p -e "SHOW DATABASES;"
echo "DONE!"
