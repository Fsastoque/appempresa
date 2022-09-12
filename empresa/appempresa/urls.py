from django.urls import path
from .views import UsuariosViews
from .views import CreaEmpresaViews

urlpatterns=[

    path('usuario/', UsuariosViews.as_view(), name="listar"),
    path('empresa/', CreaEmpresaViews.as_view(), name="listempresa")

]
