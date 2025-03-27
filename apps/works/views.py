from django.shortcuts import render, get_object_or_404

from apps.groups.models import Group
from apps.works.models import Work


def list_works_by_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    works = group.works_for_group.all()
    topics = [i.topic for i in works]
    if request.user.is_student:
        return render(request, "pages/works/list-work.html", locals())
    else:
        return render(request, "teacher/works/list-work.html", locals())
