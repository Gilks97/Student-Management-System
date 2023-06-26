"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.conf.urls.static import static

from student_management_app import views, Hodviews, StudentViews
from student_management_system import settings


urlpatterns = [

    path('demo',views.showDemoPage,),
    path('admin/', admin.site.urls),
    path('',views.ShowLoginPage, name="show_login"),
    path('get_user_details',views.GetUserDetails),
    path('logout_user',views.logout_user,),
    path('doLogin', views.doLogin, name='doLogin'),
    path('admin_home', Hodviews.admin_home, name='admin_home'),
    path('add_staff', Hodviews.add_staff, name='staff'),
    path('add_course', Hodviews.add_course, name='course'),
    path('add_course_save', Hodviews.add_course_save, name='add_course_save'),
    path('add_student', Hodviews.add_student, name='add_student'),
    path('add_student_save', Hodviews.add_student_save, name='add_student_save'),
    path('manage_student', Hodviews.manage_student, name='manage_student'),
    path('edit_student/<str:student_id>', Hodviews.edit_student, name="edit_student"),
    path('edit_student_save/', Hodviews.edit_student_save, name="edit_student_save"),
    path('delete_student/<student_id>/', Hodviews.delete_student, name="delete_student"),
    #path('add_subject', Hodviews.add_subject, name='add_subject'),
    #path('add_subject_save', Hodviews.add_subject_save, name='add_subject_save'),
    path('manage_course/', Hodviews.manage_course, name="manage_course"),
    path('edit_course/<course_id>/', Hodviews.edit_course, name="edit_course"),
    path('edit_course_save/', Hodviews.edit_course_save, name="edit_course_save"),
    path('delete_course/<course_id>/', Hodviews.delete_course, name="delete_course"),
    
    #student url path
    path('student_home/', StudentViews.student_home, name="student_home"),
    
    path('student_apply_leave', StudentViews.student_apply_leave, name="student_apply_leave"),
    path('student_apply_leave_save', StudentViews.student_apply_leave_save, name="student_apply_leave_save"),
    path('student_feedback', StudentViews.student_feedback, name="student_feedback"),
    path('student_feedback_save', StudentViews.student_feedback_save, name="student_feedback_save"),
    path('student_profile/', StudentViews.student_profile, name="student_profile"),
    path('student_profile_update/', StudentViews.student_profile_update, name="student_profile_update"),
   path('student_details/', StudentViews.student_details, name='student_details'),
    
 
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
