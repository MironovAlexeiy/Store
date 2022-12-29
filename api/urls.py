from django.urls import include, path
from rest_framework import routers

from .views import BasketModelViewSet, ProductModelVewSet

router = routers.DefaultRouter()
router.register(r'products', ProductModelVewSet)
router.register(r'baskets', BasketModelViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls), name='product-list'),
]
