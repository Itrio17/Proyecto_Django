from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    """Definición de la tabla User"""
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    fechaNacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        """Representacion de str para User"""
        return f"{self.user.username}"

