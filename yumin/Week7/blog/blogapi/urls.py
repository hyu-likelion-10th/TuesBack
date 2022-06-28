from django.urls import path, include

from blogapi.views import PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'blog', PostViewSet, basename="blog")

urlpatterns = [
    path('', include(router.urls))
]
