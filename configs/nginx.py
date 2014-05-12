from os import environ
from jinja2 import Template

from yoboard import config


print(Template('''
worker_processes 4;

events {
  worker_connections 1024;
}

http {
  include       mime.types;
  default_type  application/octet-stream;

  gzip              on;
  sendfile          on;
  keepalive_timeout 65;

  access_log {{ environ.OPENSHIFT_DIY_LOG_DIR }}/nginx.access.log;
  error_log  {{ environ.OPENSHIFT_DIY_LOG_DIR }}/nginx.errors.log;

  server {
    listen      {{ environ.OPENSHIFT_DIY_IP }}:8080;
    server_name localhost;

    location /favicon.ico {
      alias {{ environ.OPENSHIFT_REPO_DIR }}/favicon.ico;
    }

    location /static/banner {
      alias {{ config.BANNER_DIR }};
    }

    location /static/upload {
      alias {{ config.UPLOAD_DIR }};
    }

    location /static {
      alias {{ config.STATIC_DIR }};
    }

    location / {
      proxy_pass http://unix:/tmp/gunicorn.socket;
      proxy_set_header Host            $host;
      proxy_set_header X-Forwarded-For $remote_addr;
    }
  }
}
''').render(config=config, environ=environ))
