from django.shortcuts import render
from .models import Urls

# Todas as views aqui
def index(request):
	return render(request, 'index.html')

def paginas(request):
	if request.method == "POST":
		pesquisa = request.POST.get('tf_busca')
		paginas = Urls.objects.filter(url__contains=pesquisa).order_by('url')
		return render(request, 'paginas.html', {'paginas': paginas})
