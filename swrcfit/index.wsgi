"""mod_wsgi entry point for SWRC Fit.

The application deliberately keeps the CGI renderer in index.py so the web
interface has a single implementation. The Apache configuration runs this
application in a one-thread daemon because this adapter captures its legacy
print-based output.
"""

import contextlib
import io
import os
import sys

APP_DIR = os.path.dirname(os.path.abspath(__file__))
if APP_DIR not in sys.path:
    sys.path.insert(0, APP_DIR)

from index import maincgi


def application(environ, start_response):
    """Adapt the existing CGI-style renderer to the WSGI callable protocol."""
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        maincgi(environ=environ, input_stream=environ['wsgi.input'])

    cgi_headers, separator, body = output.getvalue().partition('\n\n')
    if not separator:
        # This should not occur, but return a valid WSGI response if it does.
        body = cgi_headers
        headers = [('Content-Type', 'text/html; charset=UTF-8')]
    else:
        headers = []
        for line in cgi_headers.splitlines():
            name, value = line.split(':', 1)
            headers.append((name.strip(), value.strip()))

    encoded_body = body.encode('utf-8')
    headers.append(('Content-Length', str(len(encoded_body))))
    start_response('200 OK', headers)
    return [encoded_body]
