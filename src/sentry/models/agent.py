from __future__ import absolute_import

from django.db import models
from django.utils import timezone

from sentry.db.models import Model, EncryptedTextField


class Agent(Model):
    __core__ = True

    agent_id = models.CharField(max_length=64, unique=True)

    public_key = EncryptedTextField()
    first_seen = models.DateTimeField(default=timezone.now)
    last_seen = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'sentry'
        db_table = 'sentry_agent'
