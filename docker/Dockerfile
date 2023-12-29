# Docker image of Python 3 with Debian 12 bookworm (slim version).
# Bookworm was released at 2023-06-10.
# For release information, see https://wiki.debian.org/DebianReleases
# See a list of Docker image at https://hub.docker.com/_/python
FROM python:3-slim-bookworm

# Basic system
USER root
RUN apt update
RUN apt upgrade -y

# Setup Apache
RUN apt install -y apache2
RUN apt clean
COPY ./apache2.conf /etc/apache2/apache2.conf
RUN ln -s ../mods-available/cgi.load /etc/apache2/mods-enabled/cgi.load
RUN ln -s ../mods-available/rewrite.load /etc/apache2/mods-enabled/rewrite.load

# SWRC Fit
RUN pip3 install unsatfit
RUN pip3 cache purge
RUN ln -s /usr/local/bin/python3 /usr/bin/python3

# Run Apache
EXPOSE 80
CMD ["apache2ctl", "-D","FOREGROUND"]
