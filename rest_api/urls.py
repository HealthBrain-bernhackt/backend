from rest_framework import routers

from .views import ProfileViewSet, MessageViewSet, TreatmentViewSet

router = routers.DefaultRouter()
router.register('profile', ProfileViewSet, 'profile')
router.register('message', MessageViewSet, 'message')
router.register('treatment', TreatmentViewSet, 'treatment')

urlpatterns = router.urls
