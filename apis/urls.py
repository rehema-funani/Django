from django.urls import path
from .views import StudentListViews
urlpatterns = [
    path("students/",StudentListViews.as_view(),name = "student_list_view"),
]


