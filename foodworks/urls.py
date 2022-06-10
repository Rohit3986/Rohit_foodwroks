from django.urls import path,include
from foodworks import views

#added urls for the project
urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('my_orders',views.order_history,name="my_orders"),
    path('book_your_order',views.order_booking,name="order_booking"),
]