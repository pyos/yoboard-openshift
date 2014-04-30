from os import path
from os import environ


bind        = 'unix:/tmp/gunicorn.socket'
workers     = 4
daemon      = True
preload_app = True

accesslog = path.join(environ['OPENSHIFT_DIY_LOG_DIR'], 'gunicorn.access.log')
errorlog  = path.join(environ['OPENSHIFT_DIY_LOG_DIR'], 'gunicorn.errors.log')
