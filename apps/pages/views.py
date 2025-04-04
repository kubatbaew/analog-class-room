from django.http import HttpRequest
from django.shortcuts import render, redirect


def homepage(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect("login")

    if not request.user.is_student:
        return teacher_homepage(request)

    user = request.user
    groups = user.groups_for_student.all()[::-1]

    return render(request, "pages/homepage/index.html", locals())


def teacher_homepage(request: HttpRequest):
    if not request.user.is_authenticated:
        ...

    user = request.user
    groups = user.groups_for_teacher.all()[::-1]

    return render(request, "teacher/homepage/index.html", locals())
