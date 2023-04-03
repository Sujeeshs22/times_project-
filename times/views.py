from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .forms import *
from django.contrib.auth import *
from django.http import *
from .models import *
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.


def index(request):
    return render(request, "timesproject/index.html")


def loginUser(request):
    if request.method == "POST":
        loginform = loginUserForm(request.POST)
        if loginform.is_valid():
            email = loginform.cleaned_data["email"]
            password = loginform.cleaned_data["password"]
            user = userModel.objects.filter(
                email=email, password=password)
            if len(user) > 0:
                if user[0].role == "student":
                    login(request, user[0])
                    return HttpResponseRedirect(reverse("student-page"))
                elif user[0].role == "admin":
                    login(request, user[0])
                    return HttpResponseRedirect(reverse("admin-page"))
                elif user[0].role == "staff":
                    login(request, user[0])
                    return HttpResponseRedirect(reverse("staff-page"))
                elif user[0].role == "editor":
                    login(request, user[0])
                    return HttpResponseRedirect(reverse("editor-page"))
            else:
                return HttpResponse({'error': "invalid credatianls"})
        else:
            loginform = loginUserForm(request.POST)
            return render(request, "timesproject/login.html", {"loginform": loginform})
    else:
        loginform = loginUserForm()
        return render(request, "timesproject/login.html", {"loginform": loginform})


def userSignup(request):
    if request.method == "POST":
        registerform = RegisterationForm(request.POST)
        if registerform.is_valid():
            username = registerform.cleaned_data["username"]
            role = registerform.cleaned_data["role"]
            nationality = registerform.cleaned_data["nationality"]
            country = registerform.cleaned_data["country"]
            email = registerform.cleaned_data["email"]
            phone = registerform.cleaned_data["phone"]
            password = registerform.cleaned_data["password"]
            user = userModel(username=username, role=role,
                             nationality=nationality, email=email, phone=phone, country=country, password=password)
            user.save()
            return HttpResponseRedirect(reverse("login"))
        else:
            registerform = RegisterationForm(request.POST)
            return render(request, "timesproject/register.html", {"registerform": registerform})

    else:
        registerform = RegisterationForm()
        return render(request, "timesproject/register.html", {"registerform": registerform})


def showerror(request):
    return render(request, "timesproject/error.html")


def checkadmin(user):
    if user.role == "admin":
        return True


def checkeditor(user):
    if user.role == "editor":
        return True


def checkstudent(user):
    if user.role == "student":
        return True


def checkstaff(user):
    if user.role == "staff":
        return True


@login_required(login_url=reverse_lazy("/"))
def logoutUser(request):
    logout(request)
    return HttpResponseRedirect("/")


@login_required(login_url=reverse_lazy("/"))
@user_passes_test(checkstudent, login_url=reverse_lazy("error"))
def studentPage(request):
    return render(request, "timesproject/student.html")


@login_required(login_url=reverse_lazy("/"))
@user_passes_test(checkadmin, login_url=reverse_lazy("error"))
def adminPage(request):
    return render(request, "timesproject/admin.html")


@login_required(login_url=reverse_lazy("/"))
@user_passes_test(checkstaff, login_url=reverse_lazy("error"))
def staffPage(request):
    return render(request, "timesproject/staff.html")


@login_required(login_url=reverse_lazy("/"))
@user_passes_test(checkeditor, login_url=reverse_lazy("error"))
def editorPage(request):
    return render(request, "timesproject/editor")
