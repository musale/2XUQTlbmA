"""Render the templates."""
from django.shortcuts import render


def user_list(request):
    """Render the user list template."""
    return render(request, 'core/user_list.html')
