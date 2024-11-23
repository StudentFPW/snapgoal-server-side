from rest_framework import viewsets, status
from rest_framework.response import Response
from cache_memoize import cache_memoize

from .serializers import ProductSerializer

from .extend_schema import (
    parameters_schema_decorator,
    list_products_schema_decorator,
    get_product_by_id_schema_decorator,
    create_product_schema_decorator,
)


class ProductViewSet(viewsets.ViewSet):
    serializer_class = ProductSerializer

    # @parameters_schema_decorator
    @list_products_schema_decorator
    def list(self, request):
        pass

    # @parameters_schema_decorator
    @get_product_by_id_schema_decorator
    def retrieve(self, request, *args, **kwargs):
        pass

    # @parameters_schema_decorator
    @create_product_schema_decorator
    def create(self, request):
        pass
