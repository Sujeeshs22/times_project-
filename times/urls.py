from django.urls import path
from . import views


urlpatterns = [
    path("home", views.index, name="home"),
    path("register", views.userSignup, name="register-user"),
    path("", views.loginUser, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("admin", views.adminPage, name="admin-page"),
    path("staff", views.staffPage, name="staff-page"),
    path("editor", views.editorPage, name="editor-page"),
    path("student", views.studentPage, name="student-page"),
    path("page_error", views.showerror, name="error")
]
