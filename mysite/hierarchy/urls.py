from django.urls import path

from . import views

app_name = 'hierarchy'
urlpatterns = [
    path('', views.index, name='index'),
    path('employee/<int:pk>/', views.employeedetail, name='employeedetail'),
    path('department/<int:pk>/', views.departmentdetail, name='departmentdetail'),
    path('adddept/', views.adddept, name='adddept'),
]
