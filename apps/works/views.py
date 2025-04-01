from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from apps.groups.models import Group
from apps.works.models import Work, DoneWork


def list_works_by_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    works = group.works_for_group.all()[::-1]
    topics = set([i.topic for i in works])

    if request.user.is_student:
        return render(request, "pages/works/list-work.html", locals())
    else:
        return render(request, "teacher/works/list-work.html", locals())


def detail_work(request, pk):
    work = get_object_or_404(Work, pk=pk)
    done_work_student = False
    done_work_file_name = ""

    for done_work in work.done_works.all():
        for student_work in request.user.my_done_works.all():
            if student_work == done_work:
                done_work_student = True
                done_work_file_name = done_work.file_work.name


    if request.user.is_student:
        return render(request, "pages/works/read-work.html", locals())
    else:
        return render(request, "teacher/works/read-work-teacher.html", locals())


def create_done_work(request, pk):
    work = get_object_or_404(Work, pk=pk)
    work_file = request.FILES.get("work_file")

    done_work = DoneWork.objects.create(
        student=request.user,
        work=work,
        file_work=work_file
    )
    done_work.status = "submitted"
    done_work.save()

    return redirect("detail_work", pk)


def works_students(request, pk):
    work = get_object_or_404(Work, pk=pk)

    students = work.group.students.all()
    students_done_works = DoneWork.objects.select_related('student', 'work').filter(status="submitted", work=work)
    students_done_works_grade = DoneWork.objects.select_related('student', 'work').filter(status="done_grade", work=work)
    students_not_done_works = []
    students_not_done_works_count = students.count() - (students_done_works.count() + students_done_works_grade.count())

    for student in students:
        if student in [done_work.student for done_work in students_done_works] or student in [done_work.student for done_work in students_done_works_grade]:
            ...
        else:
            students_not_done_works.append(student)

    done_st = 0
    not_done_st = 0
    actions_sort = DoneWork.StatusChoices.values
    print(actions_sort)

    for student in students:
        if any(student_work in work.done_works.all() for student_work in student.my_done_works.all()):
            done_st += 1 
        else:
            not_done_st += 1


    return render(request, "teacher/works/works-students.html", locals())


def done_work_student(request, pk):
    done_work = get_object_or_404(DoneWork, pk=pk)
    
    return render(request, "teacher/works/work-student.html", locals())


def done_work_add_grade(request, pk):
    done_work = get_object_or_404(DoneWork, pk=pk)

    done_work.grade = request.POST.get("student_grade")
    done_work.status = "done_grade"
    done_work.save()
    return redirect(f"{reverse('detail_done_work', args=[done_work.id])}?add=true")
