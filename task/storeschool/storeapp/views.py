from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Department,Details,Purpose,Course
from .forms import RegForm


# Create your views here.
def regform(request):
    data = Details.objects.all()
    form = RegForm()
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form Submission Successful')
            return redirect('/regform')
    return render(request, 'regform.html', {'form': form})

def update(request, pk):
    person = get_object_or_404(Details, pk=pk)
    form = RegForm(instance=person)
    if request.method == 'POST':
        form = RegForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/update', pk=pk)
    return render(request, 'regform.html', {'form': form})

def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'deptdropdown.html', {'courses': courses})


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'form.html')
        else:
            messages.info(request, 'Invalid credentials!Please Register Here and then Login')
            return redirect('/login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confpassword = request.POST['password1']
        if password == confpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exists")
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username,
                                                password=password)
                user.save();

                print("user created")
                return redirect('/login')
        else:
            messages.info(request, "password not matching")
            print("password is not macthing")
            return redirect('/register')

        # return redirect('/')

    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
