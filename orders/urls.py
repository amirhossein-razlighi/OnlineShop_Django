from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.create_order, name='create'),
    path('<int:order_id>/', views.order_detail, name='detail'),
]
