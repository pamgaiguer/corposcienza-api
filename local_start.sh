#!/bin/bash

# Garante que está no diretório certo
# cd /opt/corposcienza/api

#  Cria o ambiente virtual
python3 -m venv venv
# Ativa o ambiente virtual
source venv/bin/activate

# Instala as dependências
pip install --upgrade pip
pip install -r requirements.txt 

# Aplica migrações do banco de dados
# python manage.py migrate

# Inicia o servidor
python manage.py runserver