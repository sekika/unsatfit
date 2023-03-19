# Docker for SWRC Fit

This directory contains files for running SWRC Fit locally on your machine using Docker. Here is the instruction.

- Install [Docker](https://www.docker.com/) on your system and run.
- Clone this repository by `git clone https://github.com/sekika/unsatfit.git`
- Go to this directory by `cd unsatfit/docker`
- Install docker system for SWRC Fit by `make install`.
- Run the system by `make run`.
- Now SWRC Fit is running on your machine at http://localhost/
- Stop the system by `make stop`. You can run again by`make run`.
- Enter the shell of the system by `make sh`.
- Update the system by `make update`.
- To see what command is running, inspect [Makefile](Makefile).
