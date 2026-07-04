from django.urls import path
from . import views
urlpatterns = [
    path('<int:empid>/', views.employee_details, name="employee_details"),
]