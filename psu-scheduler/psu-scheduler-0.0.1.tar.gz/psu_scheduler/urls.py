from django.urls import path
from . import views

urlpatterns = [
    path('run', views.run_jobs, name='run_jobs'),
    path('test', views.test_job, name='test_job'),
    path('list', views.job_list, name='jobs'),
    path('save', views.save_job, name='save_job'),
]
