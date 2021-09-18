# Django Search System
Developed in Python, Django and saved data in MySQL<br>
Interface in Bootstrap

![Search](https://github.com/joselinosantosti/search-system/blob/master/search/static/img/busca.png)

## 1. Install all softwares:
No Linux
`apt install mysql-server mysql-client python3 -y`
`sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`
Or follow the link for others OS<br>
https://github.com/PyMySQL/mysqlclient/blob/main/README.md

`pip install MySQL-python`
`pip install MySQL-python-connector`
`pip install django`

## 2. Create a database with name search and import data from the file search.sql
`CREATE DATABASE search`

## 3. Clone this repository and extract in your computer
`git clone https://github.com/joselinosantosti/search-system.git`

## 4. Run the app with:
`python manage.py runserver`
Access in your browser the address localhost:8000

## 5. Write any word and click in search button


## Create your own application
## 1. The data preparation
* Create a Crawler for feed the database.
* Executar o Crawler para indexar as urls

# Projeto Web
## 1. Create a django project with:
`django-admin startproject search-system`

## 2. In project folder make basic configurations in settings.py file 
```
LANGUAGE_CODE = 'pt-BR'
TIME_ZONE = 'America/Sao_Paulo'
```

## 3. Crieate a app
`python manage.py startapp search`

## 4. In app folder, change the views.py file:
```
from django.shortcuts import render
from .models import Urls
```

## 5. In urls.py file create a route for pages
`path('search/', views.pages, name='pages')`

## 6. Create pages view
```
def pages(request):
	if request.method == "POST":
		search = request.POST.get('tf_busca')
		pages = Urls.objects.filter(url__contains=search).order_by('url')
		total_pag = len(pages)

		# Url list int str format
		urls = [str(url.url) for url in pages]

		return render(request, 'pages.html', {'pages': pages, 'total':total_pag})
```

## 7. Mapping MySQL database
Follow the post:<br>
https://www.treinaweb.com.br/blog/mapeando-banco-de-dados-existente-com-django/

## 8. Web Interface
Create templates folder and add pages.html file. Add following content:<br>
** Form for search
<form action="" class="form-inline" id="frm_busca" action="{% url 'pages' %}" method="post">
{% csrf_token %}

** Urls list
{% for url in paginas %}
<p>{{ url.url }}</p>
<a href="{{ url.url }}"> Titulo da pagina</a>
<p> {{ descricao }}</p>
{% endfor %}

Create static -> css, image, js folders and add files