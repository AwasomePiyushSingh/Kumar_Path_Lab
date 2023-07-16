from django.urls import path , include
from doctor import views


urlpatterns = [
    path("",views.index,name='doctor_home'),
]