from django.urls import path
from .import views
urlpatterns=[
    path("register/", views.register_classroom, name="register_classroom"),
]
