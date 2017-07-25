"""Core application models."""
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class LoggedInUser(models.Model):
    """Track a user login activities."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='logged_in_user')
