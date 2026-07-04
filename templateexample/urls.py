from django.urls import path
from .views import basic_concept, template_filters, template_conditionals

urlpatterns = [
    path('basic/', basic_concept, name="basic_concept"),
    path('template_filters/', template_filters , name="template_filters"),
    path('template_conditionals/', template_conditionals , name="template_conditionals"),
]