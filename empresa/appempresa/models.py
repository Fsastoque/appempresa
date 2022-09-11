from django.db import models

class empleados(models.Model):
    id_empleados=models.IntegerField(primary_key=True)
    nombres=models.CharField(max_length=45)
    apellidos=models.CharField(max_length=45)
    email=models.CharField(max_length=100)
    telefono=models.IntegerField()
    nombre_empresa=models.CharField(max_length=45)
    fecha_creacion=models.CharField(max_length=45)
    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.id_empleados, self.nombres, self.apellidos, self.email, self.telefono, self.nombre_empresa, self.fecha_creacion)

class roles(models.Model):
    id_rol=models.IntegerField(primary_key=True)
    nombre_rol=models.CharField(max_length=100)
    def __str__(self):
        return  "%s %s" %(self.id_rol, self.nombre_rol)

class usuarios(models.Model):
    id_usuario=models.IntegerField(primary_key=True)
    email=models.CharField(max_length=100)
    imagen=models.CharField(max_length=100)
    usuario=models.CharField(max_length=45)
    password=models.CharField(max_length=45)
    id_rol=models.ForeignKey(roles, on_delete=models.CASCADE)
    #roles=models.CharField(max_length=45)
    fecha_creado=models.DateField()
    id_empleados=models.ForeignKey(empleados, on_delete=models.CASCADE)
    def __str__(self):
        return "%s %s %s %s %s %s %s %s" % (self.id_usuario, self.email, self.imagen, self.usuario, self.password, self.roles, self.fecha_creado, self.id_empleados)

class empresas(models.Model):
    id_empresas=models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=45)
    nit=models.IntegerField()
    ciudad=models.CharField(max_length=50)
    direccion=models.CharField(max_length=45)
    telefono=models.IntegerField()
    sector=models.CharField(max_length=50)
    fecha_creacion=models.DateField()
    id_usuarios=models.ForeignKey(usuarios, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_empresas, self.nombre, self.nit, self.ciudad, self.direccion, self.telefono, self.sector, self.fecha_creacion, self.id_usuarios

class transacciones(models.Model):
    id_transaccion=models.IntegerField(primary_key=True)
    fecha_registro=models.DateField()
    concepto=models.CharField(max_length=45)
    monto=models.IntegerField()
    tipo_transaccion=models.CharField(max_length=45)
    usuario_id=models.CharField(max_length=45)
    empresas_nit=models.ForeignKey(empresas, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_transaccion, self.fecha_registro, self.concepto, self.monto, self.tipo_transaccion, self.usuario_id, self.empresas_nit


    