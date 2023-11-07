from rest_framework import routers
from account import views

app_name = 'account'  # 设置App命名空间

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'userprofile', views.UserProfileViewSet)

urlpatterns = [
    *router.urls,  # 直接包含 router.urls
]