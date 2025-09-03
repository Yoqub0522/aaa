from django.urls import path

from .views import AttendanceViewSet

urlpatterns=[
    path('',AttendanceViewSet.as_view({'get': 'list', 'post': 'create'}))
]