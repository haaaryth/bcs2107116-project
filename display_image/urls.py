from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("index", views.index, name="index"),
    path("search_student", views.search_student, name="search_student"),
    path("signup", views.signup, name="signup"),
]

urlpatterns += staticfiles_urlpatterns()

