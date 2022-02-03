"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapp import views


urlpatterns = [
    path("employees/", views.employee_list, name="employee_list"),
    path("employees/<int:pk>", views.employee_details, name="employee_details"),
    path("organizations/", views.OrganizationList.as_view(), name="org_list"),
    path("organizations/<int:pk>", views.OrganizationDetail.as_view(), name="org_list"),
    path("students/", views.StudentList.as_view(), name="student_list"),
    path("students/<int:pk>", views.StudentDetail.as_view(), name="student_list"),
]
