from django.contrib import admin
from .models import Post

#se importa el modelo Post definido
#Se registra el modelo con admin.site.register(Post)

admin.site.register(Post)
