from rest_framework import viewsets, status
from rest_framework.response import Response
from cache_memoize import cache_memoize

from .serializers import TaskSerializer, ProjectSerializer, TeamSerializer

from .extend_schema import (
    parameters_schema_decorator,
    list_task_schema_decorator,
    get_task_by_id_schema_decorator,
    create_task_schema_decorator,
    list_project_schema_decorator,
    get_project_by_id_schema_decorator,
    create_project_schema_decorator,
    list_team_schema_decorator,
    get_team_by_id_schema_decorator,
    create_team_schema_decorator,
)


class TaskViewSet(viewsets.ViewSet):
    serializer_class = TaskSerializer

    # @parameters_schema_decorator
    @list_task_schema_decorator
    def list(self, request):
        pass

    # @parameters_schema_decorator
    @get_task_by_id_schema_decorator
    def retrieve(self, request, *args, **kwargs):
        pass

    # @parameters_schema_decorator
    @create_task_schema_decorator
    def create(self, request):
        pass


class TeamViewSet(viewsets.ViewSet):
    serializer_class = TeamSerializer

    # @parameters_schema_decorator
    @list_team_schema_decorator
    def list(self, request):
        pass

    # @parameters_schema_decorator
    @get_team_by_id_schema_decorator
    def retrieve(self, request, *args, **kwargs):
        pass

    # @parameters_schema_decorator
    @create_team_schema_decorator
    def create(self, request):
        pass


class ProjectViewSet(viewsets.ViewSet):
    serializer_class = ProjectSerializer

    # @parameters_schema_decorator
    @list_project_schema_decorator
    def list(self, request):
        pass

    # @parameters_schema_decorator
    @get_project_by_id_schema_decorator
    def retrieve(self, request, *args, **kwargs):
        pass

    # @parameters_schema_decorator
    @create_project_schema_decorator
    def create(self, request):
        pass
