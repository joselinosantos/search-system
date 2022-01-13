from django.contrib import admin
from django.urls import path
from search.views import IndexView, SearchPagesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchPagesView.as_view(), name='pages')
]
