"""
URL configuration for my_tennis_club project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from .views import demo, demo1,demo2,demo3,add_student,edit_student,delete_student,sub,add_subject,edit_subject,delete_subject
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('app/', demo, name='app'),
    #path('', demo),
    path('home', demo1, name='home'),
    path('aboutus', demo2, name='about_us'),
    path('contactus', demo3, name='contact_us'),
    path('addstudent', add_student, name='addstudent'),
    path('editstudent/<int:id>', edit_student, name='editstudent'),
    path('deletestudent/<int:id>', delete_student, name='deletestudent'),
    path('showsubject', sub, name='showsubject'),
    path('addsubject',add_subject, name='addsubject'),
    path('editsubject/<int:id>', edit_subject, name='editsubject'),
    path('deletesubject/<int:id>', delete_subject, name='deletesubject'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
