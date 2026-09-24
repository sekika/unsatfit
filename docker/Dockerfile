# Docker image of Python 3 with Debian 13 trixie (slim version).
# Trixie was released at 2025-08-09.
# For release information, see https://wiki.debian.org/DebianReleases
# See a list of Docker image at https://hub.docker.com/_/python
FROM python:3-slim-trixie

# Basic system
USER root
RUN apt update && apt upgrade -y

# Setup Apache
RUN apt install -y apache2 apache2-dev build-essential && apt clean && \
    pip3 install --no-cache-dir mod_wsgi && \
    mod_wsgi-express module-config > /etc/apache2/mods-available/wsgi.load && \
    a2enmod rewrite wsgi
COPY ./apache2.conf /etc/apache2/
COPY ./swrcfit-wsgi.conf /etc/apache2/conf-available/
RUN a2enconf swrcfit-wsgi

# SWRC Fit
# mod_wsgi above is compiled for the Python supplied by the base image.
RUN pip3 install unsatfit && pip3 cache purge

# Run Apache
EXPOSE 80
CMD ["apache2ctl", "-D","FOREGROUND"]
