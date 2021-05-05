from django.urls import path, include
from rest_framework import routers

from .views import ReadOnlyNotificationViewSet

router = routers.DefaultRouter()
router.register("", ReadOnlyNotificationViewSet, basename='NotificationModel')

app_name= 'Notifications'

urlpatterns = [
    path("", include(router.urls), name='notifications')
]
