from django.urls import path

from .views import StudentViewSet

urlpatterns=[
    path('',StudentViewSet.as_view({'get': 'list', 'post': 'create'}))
]