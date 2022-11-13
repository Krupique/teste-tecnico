from django.urls import path

from . import views

urlpatterns = [
    path("", views.homePage, name='home-page'),
    path("detailed/<int:id>", views.detailedNews, name='detailed-news')
]