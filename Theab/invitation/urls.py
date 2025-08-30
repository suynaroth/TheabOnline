from rest_framework.routers import DefaultRouter
from .views import EventViewSet, GuestViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'guests', GuestViewSet)

urlpatterns = [
    path('invitation/', include(router.urls)),
]