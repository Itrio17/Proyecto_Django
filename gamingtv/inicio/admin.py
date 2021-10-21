from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "user", "fechaNacimiento")

admin.site.register(Profile, ProfileAdmin)