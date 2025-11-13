#!/bin/bash
set -e  # <- opcional, mas recomendado: se algo der erro, o script para imediatamente

# Garante que está no diretório certo
cd /opt/corposcienza/api || exit 1

# Ativa o ambiente virtual
source venv/bin/activate

# Inicia o Gunicorn com 3 workers
exec gunicorn core.wsgi:application \
  --bind 0.0.0.0:3001 \
  --workers 3 \
  --timeout 120 \
  --log-file /var/log/gunicorn_corposcienza.log \
  --access-logfile /var/log/gunicorn_corposcienza_access.log