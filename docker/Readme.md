# SWRC Fit with Docker

This directory contains files for running [SWRC Fit](https://purl.org/net/swrc/) locally on your machine using Docker. It might be useful when the server is down or you have unstable network connection. Here is the instruction.

- Install [Docker Desktop](https://www.docker.com/) (or [OrbStack](https://orbstack.dev/) if you are using Mac) on your machine and run.
- Clone this repository by `git clone https://github.com/sekika/unsatfit.git`
- Go to this directory by `cd unsatfit/docker`
- Install a system (build an image and create a container) for SWRC Fit by `make install`.
- Start the system (container) by `make start`.
- Now SWRC Fit is running on your machine at http://localhost/
- Stop the system (container) by `make stop`. You can start again by `make start`.
- Enter the shell of the system by `make sh` while the system is running.
- Update the system by `make update` while the system is running.
- Uninstall the system (remove the container and the image) by `make clean`.
- To see what command is running, inspect [Makefile](Makefile).

## Versions of Debian and Python
- The setup utilizes the [Python Docker image](https://hub.docker.com/_/python) as specified in the [Dockerfile](Dockerfile). It primarily employs the slim-tagged Python 3 image version, aligned with the most recent [Debian release](https://wiki.debian.org/DebianReleases).
- If the latest Debian version is not in use, it indicates that the author has not yet verified compatibility with the newest release.
- For the same Debian image version, the Python 3 version used in the Docker image might be updated. To upgrade to the latest image, you can reinstall the Docker image using `make clean` followed by `make install`. You can verify the version of Python running with SWRC Fit by checking the footer in the HTML output produced by SWRC Fit.
