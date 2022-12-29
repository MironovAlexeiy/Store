from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products.models import Basket, Products

from .serializers import BasketSerializer, ProductSerializer


class ProductModelVewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ('create', 'destroy', 'update'):
            self.permission_classes = (IsAdminUser, )
        return super(ProductModelVewSet, self).get_permissions()


class BasketModelViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = None

    def get_queryset(self):
        qs = super(BasketModelViewSet, self).get_queryset()
        return qs.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            product_id = request.data['product_id']
            products = Products.objects.filter(id=product_id)
            if not products.exists():
                return Response({'product_id': f'No product with id={product_id}'}, status=status.HTTP_400_BAD_REQUEST)
            obj, is_created = Basket.create_or_update(product_id, self.request.user)
            status_code = status.HTTP_201_CREATED if is_created else status.HTTP_200_OK
            serializer = self.get_serializer(obj)
            return Response(serializer.data, status=status_code)
        except KeyError:
            return Response({'product_id': 'Field <product_id> is required'}, status=status.HTTP_400_BAD_REQUEST)
