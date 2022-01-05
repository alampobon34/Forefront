from django.urls import path
from joinNowApp.views import *


urlpatterns = [
    path("join-now/",join_now , name='join-now'),

]
