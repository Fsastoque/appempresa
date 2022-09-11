from django.shortcuts import render
from django.views import View
from appempresa.models import usuarios
from django.http.response import JsonResponse

class UsuariosViews(View):
    
    def get(self, request):
        usu=list(usuarios.objects.values())
        datos={'listadousuarios':usu}
        return JsonResponse (datos)