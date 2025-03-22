from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.users.managers import UserManager


class User(AbstractUser):
    username = None

    email = models.EmailField(
        max_length=120,
        unique=True,
        verbose_name="Почта"
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name="Фамилия"
    )
    last_name = models.CharField(
        max_length=120,
        verbose_name="Имя"
    )
    father_name = models.CharField(
        max_length=120,
        verbose_name="Отчество"
    )
    is_student = models.BooleanField(
        default=True,
        verbose_name="Статус студента",
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = UserManager()

    def __str__(self):
        return self.email
    
    def get_full_name_header(self):
        return f"{self.first_name} {self.last_name[0]}. {self.father_name[0]}."
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
