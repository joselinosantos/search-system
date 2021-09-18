from django.shortcuts import render
from .models import Urls
import urllib3
from bs4 import BeautifulSoup

def index(request):
	return render(request, 'index.html')

'''
#Dados da url em cada resultado
def dados_pagina(urls):
	url = 'http://www.wikipedia.com.br'
	http = urllib3.PoolManager()
	titulos = []
	
	for u in urls:
		titulos.append(u)
		pagina = http.request('GET', u)
		sopa = BeautifulSoup(pagina.data, "lxml")
		tit = str(sopa.find_all('title')).replace('<title>','')
		titulos.append(tit)
	return titulos
'''

def pages(request):
	if request.method == "POST":
		search = request.POST.get('tf_busca')
		pages = Urls.objects.filter(url__contains=search).order_by('url')
		total_pag = len(pages)

		# Url list int str format
		#urls = [str(url.url) for url in pages]

		# Chama a funcao dados_pagina
		#titulos_web = dados_pagina(urls)
		return render(request, 'pages.html', {'pages': pages, 'total':total_pag})
