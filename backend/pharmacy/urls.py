from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductViewSet, CategoryViewSet, WarehouseViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'warehouses', WarehouseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
