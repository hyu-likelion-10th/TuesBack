from django.contrib import admin
from django.urls import path
from survey_app import views
from accounts_app import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.main, name='main'),
    path('save/', views.save, name='save'),
    path('result/<int:survey_idx>', views.result, name='result'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout')
]