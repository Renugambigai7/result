from django.shortcuts import render, redirect
from .models import register_table  # Ensure your model is named 'register_table'


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def bca(request):
    return render(request, 'bca.html')

def bsccs(request):
    return render(request, 'bsccs.html')

def result(request):
    return render(request, 'result.html')

def result1(request):
    return render(request, 'result1.html')

def admin(request):
    return render(request, 'admin.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def score(request):
    return render(request, 'score.html')

def subject(request):
    return render(request, 'subject.html')

def about(request):
    return render(request, 'About.html')


# ✅ View for saving user registration form
def register_form_submission(request):
    if request.method == "POST":
        username = request.POST.get("username")
        student_id = request.POST.get("student_id")
        password = request.POST.get("password")

        # Save to the database using model 'register_table'
        register_table.objects.create(
            username=username,
            student_id=student_id,
            password=password
        )
        return redirect('login')
    return render(request, 'register.html')


# ✅ View for checking login credentials
def login_form_submission(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')

        if register_table.objects.filter(student_id=student_id, password=password).exists():
            print("login success")
            return render(request, 'dashboard.html')
        else:
            print("login failed")
            return render(request, 'login.html')

    return render(request, 'login.html')
