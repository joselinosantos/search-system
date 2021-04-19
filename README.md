# Python Webcrowler
Developed in Python, Django and saved data in MySQL

## 1. Instale todos os software necessários:
No Linux
`apt install mysql-server mysql-client python3 -y`
`pip install django`

## 2. Desenvolvendo o Crawler
Abra o Notebook e veja o passo a passo para o desenvolvimento do Crawler.

## 3. Indexação
* Criar um banco de dados
* Criar as tabelas e relacionamentos
* Executar o Crawler para indexar as urls

# Projeto Web
## 1. Crie um projeto django com
`django-admin startproject sistema-busca`

## 2. Dentro da pasta do projeto faça as configurações básicas no arquivo settings.py
```
LANGUAGE_CODE = 'pt-BR'
TIME_ZONE = 'America/Sao_Paulo'
```

## 3. Crie uma app com o comando
`python manage.py startapp busca`

## 4. Dentro da pasta da app, altere o arquivo views da seguinte forma:
```
from django.shortcuts import render
from .models import Urls
```

## Mapeamento do banco no Django
...

## Interface Web
...
