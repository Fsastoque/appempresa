from django.urls import path
from .views import UsuariosViews

urlpatterns=[

    path('usuario/', UsuariosViews.as_view(), name="listar")

]
