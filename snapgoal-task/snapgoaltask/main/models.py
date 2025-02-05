from django.db import models


class Project(models.Model):
    STATUS_CHOICES = [
        ("open", "Open"),
        ("completed", "Completed"),
    ]

    title = models.CharField(max_length=255)
    uuid = models.UUIDField(unique=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        blank=True,
    )
    team_uuids = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.title


class Team(models.Model):
    uuid = models.UUIDField(unique=True)
    title = models.CharField(max_length=255)
    member_uuids = models.JSONField(blank=True, null=True)
    task_uuids = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    STATUS_CHOICES = [
        ("open", "Open"),
        ("in progress", "In progress"),
        ("review", "Review"),
        ("completed", "Completed"),
    ]
    uuid = models.UUIDField(unique=True)
    badge_uuid = models.UUIDField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        blank=True,
    )
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
