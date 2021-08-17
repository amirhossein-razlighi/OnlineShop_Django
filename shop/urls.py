from django.urls import path

from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]
