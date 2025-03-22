from django.http import HttpRequest
from django.shortcuts import render


def homepage(request: HttpRequest):
    if not request.user.is_authenticated:
        ...

    if not request.user.is_student:
        return teacher_homepage(request)

    user = request.user
    groups = user.groups_for_student.all()

    return render(request, "pages/homepage/index.html", locals())


def teacher_homepage(request: HttpRequest):
    if not request.user.is_authenticated:
        ...

    user = request.user
    groups = user.groups_for_teacher.all()

    return render(request, "teacher/homepage/index.html", locals())
