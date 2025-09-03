from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, StudentImageViewSet

router = DefaultRouter()
router.register("students", StudentViewSet)
router.register("student-images", StudentImageViewSet)

urlpatterns = router.urls
