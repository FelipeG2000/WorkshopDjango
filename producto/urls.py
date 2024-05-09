from .views import ProductoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos', ProductoViewSet, basename='productos')

urlpatterns = router.urls