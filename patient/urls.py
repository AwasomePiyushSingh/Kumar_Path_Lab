from django.urls import path , include
from patient import views

urlpatterns = [
   path("",views.index,name='patient_home'),
]