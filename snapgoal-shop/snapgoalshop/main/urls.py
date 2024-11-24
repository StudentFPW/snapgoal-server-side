from django.urls import path

from .viewsets import ProductViewSet

urlpatterns = [
    path(
        "products/",
        ProductViewSet.as_view({"get": "list"}),  # Список
        name="product-list",
    ),
    path(
        "product/",
        ProductViewSet.as_view({"post": "create"}),  # Создание
        name="product-create",
    ),
    path(
        "product/<uuid:product_uuid>/",
        ProductViewSet.as_view({"get": "retrieve"}),  # Детали
        name="product-detail",
    ),
    path(
        "product-update/<uuid:product_uuid>/",
        ProductViewSet.as_view({"put": "update"}),  # Обновлять
        name="product-update",
    ),
]
