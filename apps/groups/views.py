from django.shortcuts import render, get_object_or_404, redirect

from apps.groups.models import Group


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
