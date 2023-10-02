from django.contrib.auth.models import AbstractUser
from django.db import models
from catalog.models import NULLABLE
# Create your models here.


class User(AbstractUser):

    username = None

    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Почта')
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    token = models.CharField(max_length=100, verbose_name='token', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
