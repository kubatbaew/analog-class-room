from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name="Название",
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
