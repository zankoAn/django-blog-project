from django.urls import path
from .views import HomePageView, LikeView, PostDetailView


app_name = "Posts"

urlpatterns = [
    path("", HomePageView.as_view(), name="home-page"),
    path("like/<int:pk>", LikeView.as_view(), name="like-post"),
    path("posts/", HomePageView.as_view(), name="posts"),
    path("<int:year>-<int:month>-<int:day>/<int:pk>/<slug:slug>/", PostDetailView.as_view(), name="post"),
]
