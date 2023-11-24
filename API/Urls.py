from rest_framework.routers import DefaultRouter
from .views import AuthSignUp
from django.urls import path
from .views import signup
#
# router = DefaultRouter()
# router.register('Auth', AuthSignUp)
#
# urlpatterns = router.urls
urlpatterns = [
    path('api/signup/', signup, name='signup'),
]