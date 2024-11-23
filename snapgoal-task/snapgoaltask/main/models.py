from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255)
    uuid = models.UUIDField(unique=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, blank=True, null=True)
    team_uuids = models.JSONField(default=list)

    def add_team_uuid(self, team_uuid):
        if team_uuid not in self.team_uuids:
            self.team_uuids.append(str(team_uuid))

    def remove_team_uuid(self, team_uuid):
        if team_uuid in self.team_uuids:
            self.team_uuids.remove(str(team_uuid))

    def __str__(self):
        return self.title


class Team(models.Model):
    uuid = models.UUIDField(unique=True)
    title = models.CharField(max_length=255)
    member_uuids = models.JSONField(default=list)
    task_uuids = models.JSONField(default=list)

    def add_member_uuid(self, member_uuid):
        if member_uuid not in self.member_uuids:
            self.member_uuids.append(str(member_uuid))

    def remove_member_uuid(self, member_uuid):
        if member_uuid in self.member_uuids:
            self.member_uuids.remove(str(member_uuid))

    def add_task_uuid(self, task_uuid):
        if task_uuid not in self.task_uuids:
            self.task_uuids.append(str(task_uuid))

    def remove_task_uuid(self, task_uuid):
        if task_uuid in self.task_uuids:
            self.task_uuids.remove(str(task_uuid))

    def __str__(self):
        return self.title


class Task(models.Model):
    uuid = models.UUIDField(unique=True)
    badge_uuid = models.UUIDField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    due_date = models.DateField()
    assignee_id = models.UUIDField(blank=True, null=True)
    PRIORITY_CHOICES = [
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
    ]
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY_CHOICES,
        default="medium",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
