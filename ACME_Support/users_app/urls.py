from django.urls import path
from users_app import views

urlpatterns = [
    path('create/',views.create_ticket, name='create_ticket'),
    path('tickets/', views.tickets, name='tickets'),
    path("",views.SignInView.as_view(),name="signin"),
    path("user_index",views.user_index,name="user_index"),
    path("mytickets/",views.MyticketView.as_view(),name="mytickets"),
   
    

]