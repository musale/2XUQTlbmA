"""Application configuration."""
from __future__ import unicode_literals

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Application CoreConfig."""

    name = 'core'

    def ready(self):
        """Ready go."""
        import core.signals
