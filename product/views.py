from django.views import View
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from product.filter_backends import VisibleFilterBackend
from product.models import Product
from rest_framework.response import Response
from product.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (permissions.IsAdminUser,)
    filter_backends = (VisibleFilterBackend,)

    # def get_queryset(self):
    #     return Product.objects.filter(hit=True)


class Home(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        return Response({'a': 'b'})
