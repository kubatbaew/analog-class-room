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
    total_percent = (sum(total_done.grade for total_done in done_works) / total_max if (total_max := sum(max_point["work"].max_point for max_point in works)) else 1) * 100

    total_status = categorize_percentage(total_percent)
    total_percent = str(total_percent)[0:5]
    return render(request, "teacher/student/student_schedule.html", locals())


def my_schedule(request):

    if not request.user.is_authenticated:
        return redirect("login")
    
    if request.user.is_student:

        student = request.user
        groups = []

        count = 1

        for group in student.groups_for_student.all():

            done_count = 0
            for work in group.works_for_group.all():
                done_count += DoneWork.objects.select_related('student', 'work').filter(student=student, work=work).count()


            done_work_count_total = done_count
            total_percent_done = (done_count / group.works_for_group.all().count()) * 100 if done_count != 0 else 0

            if group.works_for_group.all().count() == 0:
                total_percent_done = 100

            total_status = categorize_percentage(total_percent_done)
            total_percent_done = str(total_percent_done)[0:5]
            
            groups.append(
                {
                    "count": count,
                    "group": group,
                    "done_work_count_total": done_work_count_total,
                    "total_percent_done": total_percent_done,
                    "total_status": total_status,
                }
            )
            count += 1
        
        all_works = group.works_for_group.all()
        average_percent_done = sum(float(group["total_percent_done"]) for group in groups) / len(groups) if groups else 0
        average_status_done = categorize_percentage(average_percent_done)
        average_percent_done = round(average_percent_done, 2)

        return render(request, "pages/schedules/my_schedule.html", locals())
    else:
        return redirect("login")
    