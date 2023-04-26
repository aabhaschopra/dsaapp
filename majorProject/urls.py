"""majorProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from student.views import *
from authentication.views import *
from heads.views import *
from dsa.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view),
    path('student/', student_view_data),
    path('student/<str:sid>/', student_final_view_data),
    path('accounts/', include("allauth.urls")),
    path('secy/', secy_view),
    path('secy/add_event/', secy_add_event),
    path('secy/view_proficiency/', view_proficiency),
    path('secy/<str:event_id>', event_details),
    path('secy/saveData/', secy_add_event_data, name= 'saveAddEventData'),
    path('dsa/', dsa_view),
    path('dsa/<str:event_id>', event_details),
    path('dsa/add_event/', dsa_add_event),
    re_path(r'^.*logout\/$', logout_view)
]
