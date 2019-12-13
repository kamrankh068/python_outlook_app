from django.urls import re_path
from tutorial import views

app_name = 'tutorial'
urlpatterns = [
  # The home view ('/tutorial/')
  re_path(r'^$', views.home, name='home'),
  # Explicit home ('/tutorial/home/')
  re_path(r'^home/$', views.home, name='home'),
  # Redirect to get token ('/tutorial/gettoken/')
  re_path(r'^gettoken/$', views.gettoken, name='gettoken'),
    re_path(r'^mail/$', views.mail, name='mail'),
    # Events view ('/tutorial/events/')
re_path(r'^events/$', views.events, name='events'),
# Contacts view ('/tutorial/contacts/')
re_path(r'^contacts/$', views.contacts, name='contacts'),
]