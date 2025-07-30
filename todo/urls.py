from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registerUser,name="register"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('',views.home,name="home"),
    path('task-update/<int:pk>/',views.task_Update,name="task-update"),
    path('task-delete/<int:pk>/',views.task_Delete,name="task-delete"),
]
