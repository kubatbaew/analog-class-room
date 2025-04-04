from django.db import models

from django.contrib.auth import get_user_model
from utils.get_media_path import banner_to_group

User = get_user_model()


class Group(models.Model):
    banner_img = models.ImageField(
        upload_to=banner_to_group,
        verbose_name="Баннер",
        default="default/default_banner.png"
    )
    title = models.CharField(
        max_length=120,
        verbose_name="Название",
    )
    group_title = models.CharField(
        max_length=120,
        verbose_name="Направление группы",
    )
    subject = models.CharField(
        max_length=120,
        verbose_name="Предмет",
    )
    teachers = models.ManyToManyField(
        User, related_name="groups_for_teacher",    
    )
    students = models.ManyToManyField(
        User, related_name="groups_for_student",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
