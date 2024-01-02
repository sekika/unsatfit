# Docker image of Python 3 with Debian 12 bookworm (slim version).
# Bookworm was released at 2023-06-10.
# For release information, see https://wiki.debian.org/DebianReleases
# See a list of Docker image at https://hub.docker.com/_/python
FROM python:3-slim-bookworm

# Basic system
USER root
RUN apt update && apt upgrade -y

# Setup Apache
RUN apt install -y apache2 && apt clean && \
    ln -s ../mods-available/cgi.load /etc/apache2/mods-enabled/ && \
    ln -s ../mods-available/rewrite.load /etc/apache2/mods-enabled/
COPY ./apache2.conf /etc/apache2/

# SWRC Fit
RUN pip3 install unsatfit && pip3 cache purge && \
    ln -s /usr/local/bin/python3 /usr/bin/python3

# Run Apache
EXPOSE 80
CMD ["apache2ctl", "-D","FOREGROUND"]
