from django.contrib import admin
from .views import *
from .models import *

# Register your models here
admin.site.register(Categoria)
admin.site.register(Doce)
admin.site.register(Salgado)
admin.site.register(Moda)
admin.site.register(Bebida)
admin.site.register(Gelado)
admin.site.register(Artesanato)