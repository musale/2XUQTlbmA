"""Create the URLs to be used by the talky project."""
from django.conf.urls import url

from core.views import user_list

urlpatterns = [
    url(r'^$', user_list, name='user_list'),
]
