from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    """
    后台管理账号信息
    """

    class Meta:
        verbose_name = "账号"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

