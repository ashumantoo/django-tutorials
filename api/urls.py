from django.urls import path
from . import views

urlpatterns = [
    path('people-contacts/', views.people_contacts, name="people-contacts"),
    path('people-contacts-details/<int:pk>', views.people_contacts_details, name="people-contacts-details"),

    # Using Django REST Function Based View
    path('apartments/', views.apartments_list, name="apartments"),
    path('apartment-details/<int:pk>', views.apartments_details, name="apartment-details"),

    # Using Django REST Function Based View
    path('shops/', views.ShopList.as_view(), name="shops"),
    path('shop-details/<int:pk>', views.ShopDetail.as_view(), name="shop-details"),
]
