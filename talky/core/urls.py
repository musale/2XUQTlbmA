"""Create the URLs to be used by the talky project."""
from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^$', views.user_list, name='user_list'),
    url(r'^log_in/$', views.log_in, name='log_in'),
    url(r'^log_out/$', views.log_out, name='log_out'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
]
