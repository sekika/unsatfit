# SWRC Fit

This is a source code of SWRC Fit running at https://seki.webmasters.gr.jp/swrc/

## Running by Docker
- You can run SWRC Fit locally on your machine by using Docker, which might be useful when the server is down or you have unstable network connection. Follow the instructions at [this directory](../docker).

## Requirements for setting up

- Apache is installed with [mod_wsgi](https://modwsgi.readthedocs.io/) enabled.
- [.htaccess](.htaccess) works. Check AllowOverride in the apache configuration.
- [unsatfit](https://sekika.github.io/unsatfit/) library works on the Python 3 used by mod_wsgi.

## Setup

- On the public server, obtain a release or clone the repository. For example:

  ```sh
  git clone https://github.com/sekika/unsatfit.git /srv/unsatfit
  ```

- The application directory in this example is `/srv/unsatfit/swrcfit`.
  Figures are generated in memory and embedded in the HTML response, so the
  web application does not need write access to `img/`.

## Running on an Apache server with mod_wsgi

The following example publishes this directory at `https://example.org/swrc/`.
It is self-contained and does not depend on any particular deployment host.
Replace `/srv/unsatfit/swrcfit` with the absolute application directory on
your server. The global Apache configuration below must be installed by a
server administrator; it cannot be supplied through `.htaccess`.

1. Install Apache and mod_wsgi. mod_wsgi must be built for the same Python
   major/minor version as the Python environment used below. When using a
   current Python Docker image, building mod_wsgi with `pip install mod_wsgi`
   is preferable to using a distribution package built for a different Python.

2. Create a Python environment and install the application dependency. For
   example:

   ```sh
   python3 -m venv /srv/unsatfit-venv
   /srv/unsatfit-venv/bin/python -m pip install --upgrade pip
   /srv/unsatfit-venv/bin/python -m pip install unsatfit packaging
   ```

3. Enable `mod_wsgi` and `mod_rewrite`, then add the following to Apache's
   main configuration or to the applicable virtual-host configuration. The
   `WSGIDaemonProcess` name must be unique on the server.

   ```apache
   Alias /swrc/ /srv/unsatfit/swrcfit/

   WSGIDaemonProcess swrcfit processes=1 threads=1 \
       python-home=/srv/unsatfit-venv python-path=/srv/unsatfit/swrcfit

   <Directory /srv/unsatfit/swrcfit>
       Options +ExecCGI -Indexes
       AllowOverride FileInfo Options
       Require all granted
       WSGIProcessGroup swrcfit
       WSGIApplicationGroup %{GLOBAL}
   </Directory>
   ```

   The bundled `.htaccess` selects `index.wsgi` as the directory index, maps
   it to mod_wsgi, and retains the legacy language-page rewrite rule.
   `threads=1` is intentional: the WSGI adapter captures the legacy
   print-based renderer output. Raise it only after that renderer is made
   thread-safe.

4. Reload Apache:

   ```sh
   systemctl reload apache2
   ```

## Permission

You can set up SWRC Fit anywhere if the access is restricted to a certain group of people by access control, and proper credit is clearly indicated.

To set up alternative site on servers where anyone can access, please get permission from the author. I will make a list of alternative servers.

If main [SWRC Fit](https://seki.webmasters.gr.jp/swrc/) is not accessible for more than a month and the author cannot be reached, you can take on this project by folking the repository. In that case, please clearly indicate the original author and this GitHub repository.

## Author
* Author: [Katsutoshi Seki](https://scholar.google.com/citations?user=Gs_ABawAAAAJ)
