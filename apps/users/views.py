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
    done_works = DoneWork.objects.select_related('student', 'work').filter(student=student, grade__isnull=False)

    # Считаем работу по каждому заданию
    total_grade = 0
    total_max_point = 0
    done_work_count_total = 0

    for work in group.works_for_group.all():
        done_work = DoneWork.objects.filter(student=student, work=work).first()
        if done_work is not None:
            if done_work.grade is not None:
                total_grade += done_work.grade
                total_max_point += work.max_point
                done_work_count_total += 1
        else:
            total_grade += 0
            total_max_point += work.max_point


        # Статус выполнения для каждого задания
        status_done = categorize_percentage(
            calculate_percentage(done_work.grade if done_work else None, work.max_point)
        )
        print(done_work)
        works.append(
            {
                "count": count,
                "work": work,
                "done_work": done_work,
                "status_done": status_done,
            }
        )
        count += 1

    # Теперь расчет для всей группы
    if total_max_point > 0:
        total_percent = (total_grade / total_max_point) * 100
    else:
        total_percent = 0

    total_status = categorize_percentage(total_percent)
    total_percent = str(round(total_percent, 2))

    return render(request, "teacher/student/student_schedule.html", locals())


def my_schedule(request):

    if not request.user.is_authenticated:
        return redirect("login")
    
    if request.user.is_student:

        student = request.user
        groups = []

        count = 1

        for group in student.groups_for_student.all():
            total_grade = 0
            total_max_point = 0
            done_work_count_total = 0

            for work in group.works_for_group.all():
                done_work = DoneWork.objects.filter(student=student, work=work, grade__isnull=False).first()
                if done_work:
                    total_grade += done_work.grade
                    total_max_point += work.max_point
                    done_work_count_total += 1
                else:
                    total_grade += 0
                    total_max_point += work.max_point

            if total_max_point != 0:
                total_percent_done = (total_grade / total_max_point) * 100
            else:
                total_percent_done = 0  # теперь всё правильно


            total_status = categorize_percentage(total_percent_done)
            total_percent_done = str(round(total_percent_done, 2))

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

def delete_user_is_group(request, user_pk, group_pk):
    group = get_object_or_404(Group, pk=group_pk)
    user = get_object_or_404(User, pk=user_pk)

    if user in group.students.all():
        DoneWork.objects.filter(
            student=user,
            work__group=group
        ).delete()

        group.students.remove(user)
    
    return redirect("group_users", group.id)
