import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    username = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_num = models.CharField(max_length=25)
    affiliation = models.CharField(max_length=255)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_num', 'affiliation']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Users"
        db_table = "users"


class PasswordResetModel(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=datetime.datetime.now())
    is_valid = models.BooleanField(default=True)
    reset_code = models.CharField(max_length=8)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'reset_codes'
        verbose_name_plural = 'reset_codes'
