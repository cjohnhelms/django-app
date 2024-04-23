from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'resume', views.ResumeViewSet, basename='resume')

urlpatterns = router.urls