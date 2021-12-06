from django.urls import include, path
from rest_framework import routers

from users.views import UserViewSet


router = routers.DefaultRouter()
router.register(r"users-api", UserViewSet)

app_name = "users"
urlpatterns = [
    path('', include(router.urls)),
    path('create/', UserViewSet.as_view({'post': 'create'}), name='user-create'),
    path('authenticate/', UserViewSet.as_view({'post': 'authenticate'}), name='user-authenticate')
]