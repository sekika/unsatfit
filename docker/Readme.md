# SWRC Fit with Docker

This directory contains files for running [SWRC Fit](https://seki.webmasters.gr.jp/swrc/) locally on your machine using Docker. Here is the instruction.

- Install [Docker Desktop](https://www.docker.com/) on your machine and run.
- Clone this repository by `git clone https://github.com/sekika/unsatfit.git`
- Go to this directory by `cd unsatfit/docker`
- Install a system (build an image) for SWRC Fit by `make install`.
- Run the system (create and run a container of the image) by `make run`.
- Now SWRC Fit is running on your machine at http://localhost/
- Stop the system (stop and remove the container) by `make stop`. You can run again by`make run`.
- Enter the shell of the system by `make sh` while the system is running.
- Update the system by `make update` while the system is running.
- To see what command is running, inspect [Makefile](Makefile).
