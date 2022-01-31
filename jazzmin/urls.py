from django.urls import path
from jazzmin.views import *


urlpatterns = [
    path("logout/", logout_user, name='logout'),
    path("export/<str:id>/", export, name='export'),


]