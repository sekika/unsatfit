# SWRC Fit

This is a source code of SWRC Fit running at https://seki.webmasters.gr.jp/swrc/

## Requirements for setting up

- Apache is installed with [mod_cgi](https://httpd.apache.org/docs/current/en/mod/mod_cgi.html) enabled.
- [.htaccess](.htaccess) works. Check AllowOverride in the apache configuration.
- [unsatfit](https://sekika.github.io/unsatfit/) library works on Python 3 by the user who runs cgi program on Apache.

## Setup

- Copy this directory.
- [data/server.txt](data/server.txt) has some server-dependent setup. workdir and imagefile should be writable by the user who runs cgi program on Apache.

## Permission

You can set up SWRC Fit anywhere if the access is restricted to a certain group of people by access control, and proper credit is clearly indicated.

To set up alternative site on servers where anyone can access, please get permission from the author. I will make a list of alternative servers.

If main [SWRC Fit](https://seki.webmasters.gr.jp/swrc/) is not accessible for more than a month and the author cannot be reached, you can take on this project by folking the repository. In that case, please clearly indicate the original author and this GitHub repository.

## Author
* Author: [Katsutoshi Seki](https://scholar.google.com/citations?user=Gs_ABawAAAAJ)
