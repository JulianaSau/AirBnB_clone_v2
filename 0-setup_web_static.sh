#!/usr/bin/env bash
# Bash script that sets up my web servers for the deployment of web_static

# install nginx
apt-get -y update
apt-get -y install nginx
service nginx start

# create some directories, no error if existing, make parent directories as needed
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# Create a fake HTML file (with simple content, to test your Nginx configuration)
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
   </body>
  </html>" > /data/web_static/releases/test/index.html

# Create a symbolic link. If the symbolic link already exists, 
# it should be deleted and recreated every time the script is ran
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ directory to user ubuntu and group. should be recursive for all directories in /data/ directory
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart Nginx after updating the configuration:
# Use alias inside your Nginx configuration
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default

# Restart service
service nginx restart
exit 0