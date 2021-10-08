from rest_framework import routers
from sigloChallenge.user_profiles.views.user_views import UserViewSet

router = routers.SimpleRouter()
router.register("", UserViewSet)
urlpatterns = router.urls
