from django.urls import path
from .viewsets import TaskViewSet, ProjectViewSet, TeamViewSet

urlpatterns = [
    # Project URLs
    path(
        "projects/",
        ProjectViewSet.as_view({"get": "list"}),
        name="project-list",
    ),
    path(
        "project/",
        ProjectViewSet.as_view({"post": "create"}),
        name="project-create",
    ),
    path(
        "project/<uuid:project_uuid>/",
        ProjectViewSet.as_view({"get": "retrieve"}),
        name="project-detail",
    ),
    # Team URLs
    path(
        "teams/",
        TeamViewSet.as_view({"get": "list"}),
        name="team-list",
    ),
    path(
        "team/",
        TeamViewSet.as_view({"post": "create"}),
        name="team-create",
    ),
    path(
        "team/<uuid:team_uuid>/",
        TeamViewSet.as_view({"get": "retrieve"}),
        name="team-detail",
    ),
    # Task URLs
    path(
        "tasks/",
        TaskViewSet.as_view({"get": "list"}),
        name="task-list",
    ),
    path(
        "task/",
        TaskViewSet.as_view({"post": "create"}),
        name="task-create",
    ),
    path(
        "task/<uuid:task_uuid>/",
        TaskViewSet.as_view({"get": "retrieve"}),
        name="task-detail",
    ),
]
