from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import StudentRegistrationForm,  TeacherFilterForm
from .models import Student, Teacher, Departament
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
from django.http import Http404

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('teacher_filter')
    else:
        form = StudentRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('teacher_filter')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def profile(request):
    if request.user.is_authenticated:
        student = get_object_or_404(Student, user=request.user)
        context = {
            'student': student,
            'user': request.user,
        }
        return render(request, 'profile.html', context)
    else:
        return redirect('login')

def teacher_filter_view(request):
    form = TeacherFilterForm(request.GET or None)
    teachers = Teacher.objects.none()
    
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        raise Http404 ("Student not found")

    if request.GET and form.is_valid():
        departament = form.cleaned_data.get('departament')
        interests = form.cleaned_data.get('interests')

        if departament or interests:
            if departament:
                teachers = Teacher.objects.filter(departament=departament)

            if interests:
                teachers = teachers.annotate(
                    interest_count=Count('interests', filter=Q(interests__in=interests))
                ).order_by('-interest_count')

                teachers = teachers.filter(interest_count__gt=0)

    return render(request, 'teacher_filter.html', {
        'form': form,
        'teachers': teachers,
        'student': student,
    })

def home_view(request):
    return render(request, 'home.html')