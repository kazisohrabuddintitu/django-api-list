from django.urls import path, include
from .views import APIRootView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register(r'', anotherviewclass)

urlpatterns = [
    path('api/', APIRootView.as_view(), name='api-root'),
]