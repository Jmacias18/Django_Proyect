from django.urls import path, include
from .views import CategoryViewSet, ProductViewSet,SuppliersViewSet,ProductSupplierViewSet
from rest_framework.routers import DefaultRouter

# Crear el enrutador correctamente (agregar paréntesis)
router = DefaultRouter()

# Registrar los ViewSets
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')
router.register('supplier',SuppliersViewSet, basename='supplier')
router.register('productSupplier',ProductSupplierViewSet,basename='productSupplier')

# Incluir las rutas del enrutador
urlpatterns = [
    path('', include(router.urls)),
]
