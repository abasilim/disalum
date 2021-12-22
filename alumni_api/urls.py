from rest_framework import routers, urlpatterns
from .views import UserViewset, SchoolViewset

router = routers.DefaultRouter()

router.register('user', UserViewset, basename='alumni')
router.register('school', SchoolViewset, basename='school')
#router.register('api/alumniApp', YearViewset, 'alumniApp')
urlpatterns = router.urls