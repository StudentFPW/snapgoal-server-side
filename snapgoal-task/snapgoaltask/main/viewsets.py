import uuid

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Task, Project, Team

from .serializers import TaskSerializer, ProjectSerializer, TeamSerializer

from .extend_schema import (
    parameters_schema_decorator,
    list_task_schema_decorator,
    get_task_by_id_schema_decorator,
    create_task_schema_decorator,
    update_task_schema_decorator,
    list_project_schema_decorator,
    get_project_by_id_schema_decorator,
    create_project_schema_decorator,
    update_project_schema_decorator,
    list_team_schema_decorator,
    get_team_by_id_schema_decorator,
    create_team_schema_decorator,
    update_team_schema_decorator,
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

        while True:
            new_uuid = uuid.uuid4()
            if not Project.objects.filter(uuid=new_uuid).exists():
                break

        try:
            project = Project.objects.create(
                uuid=new_uuid,
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

    @update_project_schema_decorator
    def update(self, request, *args, **kwargs):
        project_uuid = kwargs.get("project_uuid")
        project = Project.objects.filter(uuid=project_uuid).first()

        if not project:
            return Response(
                {"detail": "Project not found."}, status=status.HTTP_404_NOT_FOUND
            )

        data = request.data
        errors = {}

        if "end_date" in data and "start_date" in data:
            if data["end_date"] < data["start_date"]:
                errors["end_date"] = "End date cannot be earlier than start date."

        if "team_uuids" in data and not isinstance(data["team_uuids"], list):
            errors["team_uuids"] = "team_uuids must be a list."

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        project.title = data.get("title", project.title)
        project.description = data.get("description", project.description)
        project.start_date = data.get("start_date", project.start_date)
        project.end_date = data.get("end_date", project.end_date)
        project.status = data.get("status", project.status)
        project.team_uuids = data.get("team_uuids", project.team_uuids)

        try:
            project.save()
            serializer = self.get_serializer(project)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @list_team_schema_decorator
    def list(self, request, *args, **kwargs):
        teams = Team.objects.all()
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

        while True:
            new_uuid = uuid.uuid4()
            if not Project.objects.filter(uuid=new_uuid).exists():
                break

        try:
            team = Team.objects.create(
                uuid=new_uuid,
                title=data.get("title"),
                member_uuids=data.get("member_uuids"),
                task_uuids=data.get("task_uuids"),
            )

            serializer = self.get_serializer(team)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @update_team_schema_decorator
    def update(self, request, *args, **kwargs):
        team_uuid = kwargs.get("team_uuid")
        team = Team.objects.filter(uuid=team_uuid).first()

        if not team:
            return Response(
                {"detail": "Team not found."}, status=status.HTTP_404_NOT_FOUND
            )

        data = request.data
        errors = {}

        if "member_uuids" in data and not isinstance(data["member_uuids"], list):
            errors["member_uuids"] = "member_uuids must be a list."

        if "task_uuids" in data and not isinstance(data["task_uuids"], list):
            errors["task_uuids"] = "task_uuids must be a list."

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        team.title = data.get("title", team.title)
        team.member_uuids = data.get("member_uuids", team.member_uuids)
        team.task_uuids = data.get("task_uuids", team.task_uuids)

        try:
            team.save()
            serializer = self.get_serializer(team)
            return Response(serializer.data, status=status.HTTP_200_OK)
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

        while True:
            new_uuid = uuid.uuid4()
            if not Project.objects.filter(uuid=new_uuid).exists():
                break

        try:
            task = Task.objects.create(
                uuid=new_uuid,
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

    @update_task_schema_decorator
    def update(self, request, *args, **kwargs):
        task_uuid = kwargs.get("task_uuid")
        task = Task.objects.filter(uuid=task_uuid).first()

        if not task:
            return Response(
                {"detail": "Task not found."}, status=status.HTTP_404_NOT_FOUND
            )

        data = request.data
        errors = {}

        if "priority" in data and data["priority"] not in ["high", "medium", "low"]:
            errors["priority"] = "Priority must be one of: 'high', 'medium', 'low'."

        if "start_date" in data and "due_date" in data:
            if data["due_date"] < data["start_date"]:
                errors["due_date"] = "Due date cannot be earlier than start date."

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        task.title = data.get("title", task.title)
        task.description = data.get("description", task.description)
        task.image = data.get("image", task.image)
        task.feedback = data.get("feedback", task.feedback)
        task.badge_uuid = data.get("badge_uuid", task.badge_uuid)
        task.status = data.get("status", task.status)
        task.start_date = data.get("start_date", task.start_date)
        task.due_date = data.get("due_date", task.due_date)
        task.assignee_id = data.get("assignee_id", task.assignee_id)
        task.priority = data.get("priority", task.priority)

        try:
            task.save()
            serializer = self.get_serializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
