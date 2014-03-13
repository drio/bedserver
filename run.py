#!/usr/bin/env python

from bedserver import app
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

env_is = 'dev'

app.serve_dir = "/Users/drio/dev/bedserver/test"

if env_is == 'dev':
    app.run(debug=True)

else:
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5000)
    IOLoop.instance().start()
