#!/usr/bin/env bash
# script that sets up web servers for the deployment of web_static
apt-get -y update
apt-get -y install nginx
service start nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "My ALX Sample Codes" >/data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
exit 0
