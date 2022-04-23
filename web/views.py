from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import CreateUserForm, ProfileForm
from .models import Worker


def logoutUser(request):
    logout(request)
    return redirect('signin')


def signin(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        waiters = Worker.objects.filter(position="waiter")
        admins = Worker.objects.filter(position="admin")
        s_admin = User.objects.filter(is_superuser=True)
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect('dashboard')
                elif user.worker.position == "waiter":
                    login(request, user)
                    return redirect('room')
            else:
                messages.error(request, "Xato! Parol noto`g`ri")
                return redirect('signin')
        context = {"waiters": waiters, "s_admin": s_admin}
        return render(request, 'login.html', context)


# @login_required(login_url='/')
def dashboard(request):
    return render(request, 'dashboard.html')


# @login_required(login_url='/')
def income(request):
    return render(request, 'income.html')


@login_required(login_url='/')
def worker(request):
    if request.user.is_superuser:
        workers = Worker.objects.all()
        form = CreateUserForm()
        profil_form = ProfileForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            profil_form = ProfileForm(request.POST)
            if form.is_valid() and profil_form.is_valid():
                print("passed")
                user = form.save()
                profile = profil_form.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('worker')
            else:
                print(form.errors, '\n', profil_form.errors)
                return redirect('worker')
        context = {'form': form, 'profil_form': profil_form, 'workers': workers}
        return render(request, 'worker.html', context)
    else:
        return redirect('index')


# @login_required(login_url='/')
def product(request):
    return render(request, 'product.html')


# @login_required(login_url='/')
def table(request):
    return render(request, 'table.html')


# @login_required(login_url='/')
def order(request):
    return render(request, 'order.html')


# @login_required(login_url='/')
def document(request):
    return render(request, 'document.html')
