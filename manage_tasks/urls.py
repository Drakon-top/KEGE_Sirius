from django.urls import path

from . import views

urlpatterns = [
    path("", views.MainView.as_view()),
    path("logout", views.Logout.as_view()),
    path("login", views.LoginView.as_view()),
    path("add_answer", views.AddAnswerView.as_view()),
    path("result_answer", views.ResultView.as_view())
]