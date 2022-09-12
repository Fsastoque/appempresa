import json
from django.shortcuts import render
from django.views import View
from appempresa.models import usuarios
from appempresa.models import empresas
from appempresa.models import roles
from django.http.response import JsonResponse


class UsuariosViews(View):
    
    def get(self, request):
        usu=list(usuarios.objects.values())
        datos={'listadousuarios':usu}
        #cli=list(cliente.objects.filter)
        return JsonResponse (datos)

class CreaEmpresaViews(View):

    def post(self,request):        
        datos=json.loads(request.body)
        empresas.objects.create(documento=datos["documento"],nombre =datos["nombre"])
        return JsonResponse (datos)

        #emp=list(empresas.objects.values())
        #datos={'listadoempresa':emp}
        #return JsonResponse (datos)
        
        #serializer = SnippetSerializer(empresas,data=request.DATA)
        #obj =usuarios.query(usuarios).filter_by(id_usuario=empresas.id_usuarios).first()
        #rol=roles.objects.values(empresas.id_usuarios)
        #datos={'listadousuarios':usu}
        #return JsonResponse (empresas)