"""wechat_StuInfoSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from infosys import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login),
    path('main/', views.main),
    path('profile/', views.profile),
    path('leaves/', views.leaves),
    path('credit/', views.credit),
    path('ask/', views.ask),
    path('submit_question/', views.submit_question),
    path('watch-score-cadre-rewardpunish/', views.watch_score_cadre_rewardpunish),
    path('watch-calendar/', views.watch_calendar),


    path('teacher-main/', views.teacher_main),
    path('answer/', views.answer),
    path('write-answer/', views.write_answer),
    path('reply/', views.reply),

    path('admin-main/', views.admin_main),
    path('about-student/', views.about_student),
    path('about-teacher/', views.about_teacher),
    path('add-student/', views.add_student),
    path('apply-add-student/', views.apply_add_student),
    path('list-student/', views.list_student),
    path('modify-student/', views.modify_student),
    path('apply-modify-student/', views.apply_modify_student),
    path('apply-delete-student/', views.apply_delete_student),
    path('batch-add-student/', views.batch_add_student),
    path('apply-batch-add-student/', views.apply_batch_add_student),
    path('batch-add-credit/', views.batch_add_credit),
    path('apply-batch-add-credit/', views.apply_batch_add_credit),
    path('batch-add-leave/', views.batch_add_leave),
    path('apply-batch-add-leave/', views.apply_batch_add_leave),
    path('list-teacher/', views.list_teacher),
    path('modify-teacher/', views.modify_teacher),
    path('apply-modify-teacher/', views.apply_modify_teacher),
    path('apply-delete-teacher/', views.apply_delete_teacher),
    path('add-teacher/', views.add_teacher),
    path('apply-add-teacher/', views.apply_add_teacher),
    path('score-cadre-rewardpunish/', views.score_cadre_rewardpunish),
    path('upload-score-cadre-rewardpunish/', views.upload_score_cadre_rewardpunish),
    path('calendar/', views.calendar),
    path('upload-calendar/', views.upload_calendar),

    path('root-main/', views.root_main),
]
