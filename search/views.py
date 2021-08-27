from django.shortcuts import render
from .models import Urls
import urllib3
from bs4 import BeautifulSoup

# Todas as views aqui
def index(request):
	return render(request, 'index.html')

def dados_pagina(urls):
	url = 'http://www.iaexpert.com.br'
	http = urllib3.PoolManager()
	titulos = []
	
	for u in urls:
		titulos.append(u)
		pagina = http.request('GET', u)
		sopa = BeautifulSoup(pagina.data, "lxml")
		tit = str(sopa.find_all('title')).replace('<title>','')
		titulos.append(tit)
	return titulos

def paginas(request):
	if request.method == "POST":
		tit = "Titulo da pagina"
		desc = "Breve descricao da página web"
		pesquisa = request.POST.get('tf_busca')
		paginas = Urls.objects.filter(url__contains=pesquisa).order_by('url')
		total_pag = len(paginas)

		# Lista de urls em formato str
		urls = [str(url.url) for url in paginas]

		# Chama a funcao dados_pagina
		titulos_web = dados_pagina(urls)
		return render(request, 'paginas.html', {'paginas': paginas, 'titulos_web':titulos_web, 'titulo':tit, 'descricao':desc, 'total':total_pag})
