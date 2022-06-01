from django.contrib import admin
from django.urls import path
from vote import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("auth/login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("auth/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("save/<int:Id>/", views.save, name="save"),
    path("result/<int:Id>/", views.result, name="result"),

]
