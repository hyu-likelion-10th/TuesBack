
from django.contrib import admin
from django.urls import path
from vote import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("result/", views.result, name="result"),
    path("question/", views.question, name="question"),
    path("add/<str:question>/", views.add),
]
