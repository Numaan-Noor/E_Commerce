from rest_framework.routers import DefaultRouter
from .views import AuthSignUp

router = DefaultRouter()
router.register('items', AuthSignUp)

urlpatterns = router.urls
