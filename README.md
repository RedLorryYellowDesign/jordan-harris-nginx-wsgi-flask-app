# Compose Sample Application

## NGINX Reverse Proxy -> WSGI -> Python/Flask Backend

Project structure:

```text
.
├── compose.yaml
├── flask
│   ├── app.py
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── projects.html
│   │   └── admin
│   │   |   └── index.html
│   ├── Dockerfile
│   ├── requirements.txt
│   └── wsgi.py
└── nginx
    ├── default.conf
    ├── Dockerfile
    ├── nginx.conf
    └── start.sh
```
