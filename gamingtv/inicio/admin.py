from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "nombre", "apellidos", "email", "fechaNacimiento", "tipo")

admin.site.register(User, UserAdmin)