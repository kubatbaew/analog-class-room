from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model

from apps.groups.models import Group

User = get_user_model()


def edit_group(request, pk):
    group = get_object_or_404(Group, pk=pk)

    group.title = request.POST['title']
    group.subject = request.POST['subject']
    group.group_title = request.POST['groupName']
    group.save()

    return redirect('homepage')


def delete_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.delete()

    return redirect('homepage')


def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)

    if request.user.is_student:
        if request.user not in group.students.all():
            return redirect('homepage')

    return render(request, "pages/group/detail-group.html", locals())


def change_banner_group(request, pk):
    group = get_object_or_404(Group, pk=pk)

    if request.method == "POST":
        print(request.FILES)
        group.banner_img = request.FILES["banner_img"]
        group.save()

        return redirect("detail_group", group.id)

    return render(request, "pages/group/change-banner.html", locals())


def group_users(request, pk):
    group = get_object_or_404(Group, pk=pk)

    return render(request, "pages/group/group_users.html", locals())


def add_student_to_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    student_email = request.POST.get("student_username")
    try:
        student = User.objects.get(email=student_email)

        group.students.add(student)
    except User.DoesNotExist:
        ...
    finally:
        return redirect("group_users", pk)
