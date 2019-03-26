from django.urls import path, include
from .views import CategoryViewSet, PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'', xViewSet, basename='')
router.register(r'', yViewSet, basename='')
urlpatterns = router.urls
