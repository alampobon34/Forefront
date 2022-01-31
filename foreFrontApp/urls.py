from django.urls import path
from foreFrontApp.views import *


urlpatterns = [
    path("", index, name='home'),
    path("about-us/", about_us, name='about-us'),
    path("news-details/<int:id>/", news_details, name='news-details'),
    path("subscribe", subscribe, name='subscribe'),

]
