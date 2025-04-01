from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import logout, authenticate, login, get_user_model

from apps.groups.models import Group
from apps.works.models import DoneWork
from utils.calculate_schedule import calculate_percentage, categorize_percentage

User = get_user_model()


def logout_logics(request):
    logout(request)
    return redirect('login')


def login_logics(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')

        error = "Неправильный логин или пароль!"
        return render(request, 'pages/auth/login.html', locals())

    return render(request, 'pages/auth/login.html', locals())


def student_schedule(request, pk, group_pk):
    group = get_object_or_404(Group, pk=group_pk)
    student = get_object_or_404(User, pk=pk)
    works = []
    count = 1
    done_works = DoneWork.objects.select_related('student', 'work').filter(student=student)

    for work in group.works_for_group.all():
        done_work = DoneWork.objects.select_related('student', 'work').filter(student=student, work=work)
        status_done = categorize_percentage(calculate_percentage(done_work.first().grade if done_work.first() else None, work.max_point))
        works.append(
            {
                "count": count,
                "work": work,
                "done_work": done_work,
                "status_done": status_done,
            }
        )
        count += 1
    total_percent = (sum(total_done.grade for total_done in done_works) / sum(max_point["work"].max_point for max_point in works)) * 100
    total_status = categorize_percentage(total_percent)
    total_percent = str(total_percent)[0:5]
    return render(request, "teacher/student/student_schedule.html", locals())
