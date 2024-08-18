from django.urls import path
from api import views

urlpatterns = [
    path("create", views.CreateProductView.as_view()),
    path("list", views.ListProductsView.as_view()),
    path("add", views.AddStockView.as_view()),
    path("add", views.DeleteProductView.as_view()),
     

]