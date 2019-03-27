from django.urls import path, include
from .views import TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'Task', TaskViewSet, basename='Task')
#router.register(r'', yViewSet, basename='')
urlpatterns = router.urls
