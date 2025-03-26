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
