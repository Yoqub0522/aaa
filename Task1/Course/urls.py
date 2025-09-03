from django.urls import path

from .views import CourseViewSet

urlpatterns=[
    path('',CourseViewSet.as_view({'get': 'list', 'post': 'create'}))
]