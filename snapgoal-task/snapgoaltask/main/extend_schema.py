from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiResponse,
    OpenApiTypes,
)

from .serializers import (
    TaskSerializer,
    ProjectSerializer,
    TeamSerializer,
)


parameters_schema_decorator = extend_schema(
    parameters=[
        OpenApiParameter(
            name="Authorization-ID",
            type=OpenApiTypes.UUID,
            location=OpenApiParameter.HEADER,
            required=True,
            description="Токен авторизации",
        ),
    ]
)

project_schema = {
    "type": "object",
    "properties": {
        "uuid": {
            "type": "string",
            "format": "uuid",
            "example": "d47e7f97-2f3b-4236-b234-e5c1f487f0bf",
        },
        "title": {"type": "string", "example": "Project Alpha"},
        "description": {
            "type": "string",
            "example": "A detailed description of the project and its goals.",
        },
        "start_date": {"type": "string", "format": "date", "example": "2024-01-01"},
        "end_date": {"type": "string", "format": "date", "example": "2024-12-31"},
        "status": {"type": "string", "example": "active"},
        "teams": {
            "type": "array",
            "items": {"type": "string", "format": "uuid"},
            "example": [
                "550e8400-e29b-41d4-a716-446655440000",
                "550e8400-e29b-41d4-a716-446655440000",
            ],
        },
    },
}

list_project_schema_decorator = extend_schema(
    tags=["Project"],
    responses={
        200: OpenApiResponse(
            response=project_schema,
        )
    },
)

get_project_by_id_schema_decorator = extend_schema(
    tags=["Project"],
    responses={
        200: OpenApiResponse(
            response=project_schema,
        )
    },
)

create_project_schema_decorator = extend_schema(
    tags=["Project"],
    request=ProjectSerializer,
    responses={
        200: OpenApiResponse(
            response=project_schema,
        )
    },
)

update_project_schema_decorator = extend_schema(
    tags=["Project"],
    request=ProjectSerializer,
    responses={
        200: OpenApiResponse(
            response=project_schema,
        )
    },
)

team_schema = {
    "type": "object",
    "properties": {
        "uuid": {
            "type": "string",
            "format": "uuid",
            "example": "d47e7f97-2f3b-4236-b234-e5c1f487f0bf",
        },
        "title": {"type": "string", "example": "Phase 1 Team"},
        "members": {
            "type": "array",
            "items": {"type": "string", "format": "uuid"},
            "example": [
                "550e8400-e29b-41d4-a716-446655440000",
                "550e8400-e29b-41d4-a716-446655440001",
            ],
        },
        "tasks": {
            "type": "array",
            "items": {"type": "string", "format": "uuid"},
            "example": [
                "550e8400-e29b-41d4-a716-446655440000",
                "550e8400-e29b-41d4-a716-446655440001",
            ],
        },
    },
}

list_team_schema_decorator = extend_schema(
    tags=["Team"],
    responses={
        200: OpenApiResponse(
            response=team_schema,
        )
    },
)

get_team_by_id_schema_decorator = extend_schema(
    tags=["Team"],
    responses={
        200: OpenApiResponse(
            response=team_schema,
        )
    },
)

create_team_schema_decorator = extend_schema(
    tags=["Team"],
    request=TeamSerializer,
    responses={
        200: OpenApiResponse(
            response=team_schema,
        )
    },
)

update_team_schema_decorator = extend_schema(
    tags=["Team"],
    request=TeamSerializer,
    responses={
        200: OpenApiResponse(
            response=team_schema,
        )
    },
)

task_schema = {
    "type": "object",
    "properties": {
        "uuid": {
            "type": "string",
            "format": "uuid",
        },
        "title": {
            "type": "string",
            "example": "Complete Documentation",
        },
        "description": {
            "type": "string",
            "example": "Write detailed documentation for the project.",
        },
        "image": {
            "type": "string",
            "example": "https://example.com/images/task.png",
        },
        "feedback": {
            "type": "string",
            "example": "text",
        },
        "badge_uuid": {
            "type": "string",
            "example": "550e8400-e29b-41d4-a716-446655440000",
        },
        "priority": {
            "type": "string",
            "enum": ["high", "medium", "low"],
            "example": "high",
        },
        "status": {
            "type": "string",
            "example": "not started",
        },
        "start_date": {
            "type": "string",
            "format": "date",
            "example": "2024-01-01",
        },
        "due_date": {
            "type": "string",
            "format": "date",
            "example": "2024-02-01",
        },
        "assignee_id": {
            "type": "string",
            "example": "550e8400-e29b-41d4-a716-446655440000",
        },
    },
}

list_task_schema_decorator = extend_schema(
    tags=["Task"],
    responses={
        200: OpenApiResponse(
            response=task_schema,
        )
    },
)

get_task_by_id_schema_decorator = extend_schema(
    tags=["Task"],
    responses={
        200: OpenApiResponse(
            response=task_schema,
        )
    },
)

create_task_schema_decorator = extend_schema(
    tags=["Task"],
    request=TaskSerializer,
    responses={
        200: OpenApiResponse(
            response=task_schema,
        )
    },
)

update_task_schema_decorator = extend_schema(
    tags=["Task"],
    request=TaskSerializer,
    responses={
        200: OpenApiResponse(
            response=task_schema,
        )
    },
)
