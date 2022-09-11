from django.contrib import admin

from appempresa.models import empleados, usuarios, empresas, transacciones, roles

admin.site.register(empleados)
admin.site.register(usuarios)
admin.site.register(empresas)
admin.site.register(transacciones)
admin.site.register(roles)

