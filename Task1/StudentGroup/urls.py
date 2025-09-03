from django.urls import path

from .views import StudentGroupViewSet

urlpatterns=[
    path('',StudentGroupViewSet.as_view({'get': 'list', 'post': 'create'}))
]