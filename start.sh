#!/bin/bash

# Garante que está no diretório certo
cd /opt/corposcienza/api

# Ativa o ambiente virtual
source venv/bin/activate

# Inicia o Gunicorn com workers
exec gunicorn core.wsgi:application \
  --bind 0.0.0.0:3001 \
  --workers 3
