
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from piripirifood import views

urlpatterns = [
    path('admin/', admin.site.urls),

    url('categorias/$', views.CategoriaList.as_view(), name='categoria-list'),
    url('estabelecimentos/$', views.EstabelecimentoList.as_view(), name='estabelecimento-list'),

]
