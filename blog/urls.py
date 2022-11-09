from urllib.request import url2pathname
from django.urls import path
from .views import BlogHomePage, UpdateHomePage

urlpatterns = [
    path('', BlogHomePage.as_view(), name='index'),
    path('', UpdateHomePage.as_view(), name='update'),
]
