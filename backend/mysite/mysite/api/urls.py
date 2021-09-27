from rest_framework import routers
from mysite.api.views import TankViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'tanks', TankViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]