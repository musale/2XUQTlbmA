"""Hook into django signals."""
from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver

from core.models import LoggedInUser


@receiver(user_logged_in)
def on_user_login(sender, **kwargs):
    """Create a LoggedInUser object when a user logs in."""
    LoggedInUser.objects.get_or_create(user=kwargs.get('user'))


@receiver(user_logged_out)
def on_user_logout(sender, **kwargs):
    """Delete LoggedInUser object when user logs out."""
    LoggedInUser.objects.filter(user=kwargs.get('user')).delete()
