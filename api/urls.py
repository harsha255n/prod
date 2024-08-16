from django.urls import path
from api import views

urlpatterns = [
    path("create", views.CreateProductView.as_view()),
   
     

]