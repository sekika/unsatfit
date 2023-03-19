# Docker image of Python 3 with Debian 11 bullseye (slim version).
# See Debian release information at https://wiki.debian.org/DebianReleases
# See if newer image is availabe at https://hub.docker.com/_/python
FROM python:3-slim-bullseye

# Basic system
USER root
WORKDIR /var/www
RUN apt update
RUN apt upgrade -y
RUN apt install -y vim less

# Setup Apache
RUN apt install -y apache2
RUN apt clean
COPY ./apache2.conf /etc/apache2/apache2.conf
RUN ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enabled/
RUN ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/

# SWRC Fit
RUN pip3 install unsatfit
RUN ln -s /usr/local/bin/python3 /usr/bin/python3
RUN rm -rf /var/www/html

# Run Apache
EXPOSE 80
CMD ["apache2ctl", "-D","FOREGROUND"]
