from django.conf.urls import url, include

from . import views

app_name = 'api'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    
    # ex: /api/eventos
    url(r'eventos/$', views.list_events, name='eventos'),

    # /api/itens
    url(r'itens/$', views.list_itens, name='itens'),
]