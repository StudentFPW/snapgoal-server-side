from rest_framework import serializers


class ProjectSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=True)
    uuid = serializers.UUIDField(required=False)
    start_date = serializers.DateField(required=True)
    end_date = serializers.DateField(required=True)
    status = serializers.ChoiceField(
        choices=["open", "complete"],
        default="open",
        required=False,
    )
    description = serializers.CharField(max_length=1024, required=True)
    team_uuids = serializers.ListField(required=False)


class TeamSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(required=False)
    title = serializers.CharField(max_length=255, required=True)
    member_uuids = serializers.ListField(required=False)
    task_uuids = serializers.ListField(required=False)


class TaskSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(required=False)
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(required=True)
    image = serializers.URLField(required=False)
    feedback = serializers.CharField(required=False)
    badge_uuid = serializers.UUIDField(required=True)
    status = serializers.ChoiceField(
        choices=["open", "in progress", "review", "complete"],
        default="open",
        required=False,
    )
    start_date = serializers.DateField(required=True)
    due_date = serializers.DateField(required=True)
    assignee_id = serializers.UUIDField(required=False)
    priority = serializers.ChoiceField(
        choices=["high", "medium", "low"],
        required=False,
    )
