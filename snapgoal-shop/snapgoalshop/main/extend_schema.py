from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
)

from .serializers import (
    ProductSerializer,
)

product_schema = {
    "type": "object",
    "properties": {
        "uuid": {
            "type": "string",
            "format": "uuid",
        },
        "title": {
            "type": "string",
        },
        "description": {
            "type": "string",
        },
        "price": {
            "type": "integer",
        },
        "image": {
            "type": "string",
            "format": "uri",
        },
        "category": {
            "type": "string",
        },
        "availability": {
            "type": "boolean",
        },
        "feedback": {
            "type": "string",
        },
    },
}

list_products_schema_decorator = extend_schema(
    tags=["Product"],
    responses={
        200: OpenApiResponse(
            response=product_schema,
        )
    },
)

get_product_by_id_schema_decorator = extend_schema(
    tags=["Product"],
    responses={
        200: OpenApiResponse(
            response=product_schema,
        )
    },
)

create_product_schema_decorator = extend_schema(
    tags=["Product"],
    request=ProductSerializer,
    responses={
        200: OpenApiResponse(
            response=product_schema,
        )
    },
)

update_product_schema_decorator = extend_schema(
    tags=["Product"],
    request=ProductSerializer,
    responses={
        200: OpenApiResponse(
            response=product_schema,
        )
    },
)
