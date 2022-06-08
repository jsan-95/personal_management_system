import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


def custom_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return filename


class CustomUser(AbstractUser):
    name = models.CharField(max_length=250)
    avatar = models.ImageField(null=True, blank=True, upload_to=custom_path)
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'User {self.name.lower()}'
