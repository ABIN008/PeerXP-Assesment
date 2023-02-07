from django.urls import path
from admin_app import views
# from users_app import views
urlpatterns=[
    path("admin_index/",views.index,name="admin_index"),
    path("adminhome/",views.list_ticket,name="listticket"),
    path("creatuser/",views.Adduser,name="createuser"),
    path("adddept/",views.Adddepartment,name="adddept"),
    path("dept_list/",views.list_dept,name="dept_list"),
    path("update_dept/<int:id>/",views.update_dept,name="update_dept"),
    path("delete_dept/<int:id>/",views.delete_dept,name="delete_dept"),
    path("delete_ticket/<int:id>/",views.delete_ticket,name="delete_ticket"),
   

]
