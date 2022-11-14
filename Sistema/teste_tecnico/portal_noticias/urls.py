from django.urls import path

from . import views

urlpatterns = [
    path("", views.homePage, name='home-page'),
    path("detailed/<int:id>", views.detailedNews, name='detailed-news'),
    path("detailed/postComment", views.postComment, name='post-comment'),
    path("detailed/loadComments", views.loadComments, name='load-comments')
]