from django.shortcuts import render
from .models import Urls
import urllib3

# Todas as views aqui
def index(request):
	return render(request, 'index.html')

def paginas(request):
	if request.method == "POST":
		titulo = "Titulo da pagina"
		pesquisa = request.POST.get('tf_busca')
		paginas = Urls.objects.filter(url__contains=pesquisa).order_by('url')
		total_pag = len(paginas)
		return render(request, 'paginas.html', {'paginas': paginas, 'titulo':titulo})
