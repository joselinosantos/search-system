from django.shortcuts import render
from .models import Urls
import datetime
import time

YEAR = datetime.date.today().year

def index(request):
	return render(request, 'index.html', {'year': YEAR})

def pages(request):
	if request.method == "POST":
		t0 = time.time()
		search = request.POST.get('input-busca')
		pages = Urls.objects.filter(url__icontains=search).order_by('url')
		total_pag = len(pages)
		t1 = time.time()
		total_time = round(t1-t0, 2)

		return render(request, 'pages.html', {'search': search, 'pages': pages, 'total': total_pag, 'total_time': total_time, 'year':YEAR})
