from django.db import models

from django.contrib.auth import get_user_model

from apps.groups.models import Group
from apps.works.models import Work

User = get_user_model()


class Notification(models.Model):
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE,
        verbose_name="Группа",
        related_name="all_notifications",
    )
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name="Преподователь",
    )
    work = models.ForeignKey(
        Work, on_delete=models.CASCADE,
        verbose_name="Задание",
    )
    is_new_work = models.BooleanField(
        default=None,
        verbose_name="Статус нового задания",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group.title
    
    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"
