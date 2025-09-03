from django.urls import path

from .views import GroupViewSet

urlpatterns=[
    path('',GroupViewSet.as_view({'get': 'list', 'post': 'create'}))
]