from django.db import models

from django.contrib.auth import get_user_model
from apps.groups.models import Group

User = get_user_model()


class Work(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name="Название",
    )
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="works_for_teacher",
    )
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE,
        related_name="works_for_group",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время добавления",
    )
    delivery_time = models.DateTimeField(
        verbose_name="Время выполнение",
    )
    max_point = models.PositiveSmallIntegerField(
        verbose_name="Максимальное количество баллов",
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    # TODO! links = // soon!

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Домашнее задание"
        verbose_name_plural = "Домашнее задания"
