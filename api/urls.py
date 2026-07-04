from django.urls import path
from . import views
urlpatterns = [
    path('people-contacts/', views.people_contacts, name="people-contacts"),
    path('people-contacts-details/<int:pk>', views.people_contacts_details, name="people-contacts-details"),
]