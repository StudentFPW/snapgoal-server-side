import uuid

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

from .extend_schema import (
    parameters_schema_decorator,
    list_products_schema_decorator,
    get_product_by_id_schema_decorator,
    create_product_schema_decorator,
    update_product_schema_decorator,
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @list_products_schema_decorator
    def list(self, request, *args, **kwargs):
        filter_params = request.query_params
        products = Product.objects.all()

        if "category" in filter_params:
            products = products.filter(category=filter_params["category"])

        if "availability" in filter_params:
            availability = filter_params["availability"].lower() == "true"
            products = products.filter(availability=availability)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @get_product_by_id_schema_decorator
    def retrieve(self, request, *args, **kwargs):
        product_uuid = kwargs.get("product_uuid")
        product = Product.objects.filter(uuid=product_uuid).first()

        if not product:
            return Response(
                {"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(product)
        return Response(serializer.data)

    @create_product_schema_decorator
    def create(self, request, *args, **kwargs):
        data = request.data
        errors = {}
        required_fields = ["title", "price", "image"]

        for field in required_fields:
            if field not in data:
                errors[field] = f"{field} is required."

        if "price" in data and data["price"] <= 0:
            errors["price"] = "Price must be a positive integer."

        if "image" in data and not data["image"].startswith("http"):
            errors["image"] = "Image URL must start with 'http' or 'https'."

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        while True:
            new_uuid = uuid.uuid4()
            if not Product.objects.filter(uuid=new_uuid).exists():
                break

        try:
            product = Product.objects.create(
                uuid=new_uuid,
                title=data.get("title"),
                description=data.get("description"),
                price=data.get("price"),
                image=data.get("image"),
                category=data.get("category"),
                availability=data.get("availability", True),
                feedback=data.get("feedback"),
            )

            serializer = self.get_serializer(product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @update_product_schema_decorator
    def update(self, request, *args, **kwargs):
        product_uuid = kwargs.get("product_uuid")
        product = Product.objects.filter(uuid=product_uuid).first()

        if not product:
            return Response(
                {"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND
            )

        data = request.data
        errors = {}

        if "price" in data and data["price"] <= 0:
            errors["price"] = "Price must be a positive integer."

        if "image" in data and not data["image"].startswith("http"):
            errors["image"] = "Image URL must start with 'http' or 'https'."

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        product.title = data.get("title", product.title)
        product.description = data.get("description", product.description)
        product.price = data.get("price", product.price)
        product.image = data.get("image", product.image)
        product.category = data.get("category", product.category)
        product.availability = data.get("availability", product.availability)
        product.feedback = data.get("feedback", product.feedback)
        product.save()

        serializer = self.get_serializer(product)
        return Response(serializer.data)
