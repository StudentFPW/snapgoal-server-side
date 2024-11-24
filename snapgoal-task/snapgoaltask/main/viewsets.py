from rest_framework import viewsets, status
from rest_framework.response import Response
from cache_memoize import cache_memoize

from .models import Task, Project, Team

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


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @list_project_schema_decorator
    def list(self, request, *args, **kwargs):
        filter_params = request.query_params
        projects = Project.objects.all()

        if "status" in filter_params:
            projects = projects.filter(status=filter_params["status"])

        if "ordering" in filter_params:
            ordering_fields = filter_params["ordering"].split(",")
            projects = projects.order_by(*ordering_fields)

        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @get_project_by_id_schema_decorator
    def retrieve(self, request, *args, **kwargs):
        project_uuid = kwargs.get("project_uuid")
        project = Project.objects.filter(uuid=project_uuid).first()

        if not project:
            return Response(
                {"detail": "Project not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(project)
        return Response(serializer.data)

    @create_project_schema_decorator
    def create(self, request, *args, **kwargs):
        data = request.data
        errors = {}
        required_fields = ["title", "description", "start_date", "end_date"]

        for field in required_fields:
            if field not in data:
                errors[field] = f"{field} is required."

        if "start_date" in data and "end_date" in data:
            if data["end_date"] < data["start_date"]:
                errors["end_date"] = "End date cannot be earlier than start date."

        if not isinstance(data.get("team_uuids", []), list):
            errors["team_uuids"] = "team_uuids must be a list."

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            project = Project.objects.create(
                uuid=data.get("uuid"),
                title=data.get("title"),
                description=data.get("description"),
                start_date=data.get("start_date"),
                end_date=data.get("end_date"),
                status=data.get("status"),
                team_uuids=data.get("team_uuids"),
            )

            serializer = self.get_serializer(project)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @list_team_schema_decorator
    def list(self, request, *args, **kwargs):
        filter_params = request.query_params
        teams = Team.objects.all()

        # Example filter: filter teams based on title
        if "title" in filter_params:
            teams = teams.filter(title__icontains=filter_params["title"])

        # Example ordering: order teams based on the title
        if "ordering" in filter_params:
            ordering_fields = filter_params["ordering"].split(",")
            teams = teams.order_by(*ordering_fields)

        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    @get_team_by_id_schema_decorator
    def retrieve(self, request, *args, **kwargs):
        team_uuid = kwargs.get("team_uuid")
        team = Team.objects.filter(uuid=team_uuid).first()

        if not team:
            return Response(
                {"detail": "Team not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(team)
        return Response(serializer.data)

    @create_team_schema_decorator
    def create(self, request, *args, **kwargs):
        data = request.data
        errors = {}
        required_fields = ["title"]

        for field in required_fields:
            if field not in data:
                errors[field] = f"{field} is required."

        if not isinstance(data.get("member_uuids", []), list):
            errors["member_uuids"] = "member_uuids must be a list."

        if not isinstance(data.get("task_uuids", []), list):
            errors["task_uuids"] = "task_uuids must be a list."

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            team = Team.objects.create(
                uuid=data.get("uuid"),
                title=data.get("title"),
                member_uuids=data.get("member_uuids"),
                task_uuids=data.get("task_uuids"),
            )

            serializer = self.get_serializer(team)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @list_task_schema_decorator
    def list(self, request, *args, **kwargs):
        filter_params = request.query_params
        tasks = Task.objects.all()
        if "status" in filter_params:
            tasks = tasks.filter(status=filter_params["status"])
        if "priority" in filter_params:
            tasks = tasks.filter(priority=filter_params["priority"])
        if "assignee_id" in filter_params:
            tasks = tasks.filter(assignee_id=filter_params["assignee_id"])
        if "ordering" in filter_params:
            ordering_fields = filter_params["ordering"].split(
                ","
            )  # Multiple fields can be ordered by comma
            tasks = tasks.order_by(*ordering_fields)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    @get_task_by_id_schema_decorator
    def retrieve(self, request, *args, **kwargs):
        task_uuid = kwargs.get("task_uuid")
        task = Task.objects.filter(uuid=task_uuid).first()

        if not task:
            return Response(
                {"detail": "Task not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @create_task_schema_decorator
    def create(self, request, *args, **kwargs):
        data = request.data
        errors = {}
        required_fields = [
            "title",
            "description",
            "badge_uuid",
            "start_date",
            "due_date",
        ]
        for field in required_fields:
            if field not in data:
                errors[field] = f"{field} is required."

        if "start_date" in data and "due_date" in data:
            if data["due_date"] < data["start_date"]:
                errors["due_date"] = "Due date cannot be earlier than start date."

        if "priority" in data and data["priority"] not in ["high", "medium", "low"]:
            errors["priority"] = "Priority must be one of: 'high', 'medium', 'low'."

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            task = Task.objects.create(
                uuid=data.get("uuid"),
                title=data.get("title"),
                description=data.get("description"),
                image=data.get("image"),
                feedback=data.get("feedback"),
                badge_uuid=data.get("badge_uuid"),
                status=data.get("status"),
                start_date=data.get("start_date"),
                due_date=data.get("due_date"),
                assignee_id=data.get("assignee_id"),
                priority=data.get("priority"),
            )

            serializer = self.get_serializer(task)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
