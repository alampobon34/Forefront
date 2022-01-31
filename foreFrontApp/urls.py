from django.urls import path
from foreFrontApp.views import *


urlpatterns = [
    
    path('about-us/', about_us, name='about_us'),
    path('news-details/<int:id>/', news_details, name='news_details'),
    path('subscribe', subscribe, name='subscribe'),

]
