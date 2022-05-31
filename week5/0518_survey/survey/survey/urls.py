from django.contrib import admin
from django.urls import path
from survey_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.main, name='main'),
    path('save_survey/', views.save_survey, name='save_survey'),
    path('result/<int:survey_idx>', views.result, name='result'),
]
