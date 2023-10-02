from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    LikePostView,
    UnlikePostView,
    # AnalyticsView,
)

urlpatterns = [
    path(
        "posts/",
        PostListView.as_view(),
        name="post-list"),

    path(
        "posts/<int:pk>/",
        PostDetailView.as_view(),
        name="post-detail"
    ),

    path(
        "posts/<int:pk>/like/",
        LikePostView.as_view(),
        name="like-post"
    ),

    path(
        "posts/<int:pk>/unlike/",
        UnlikePostView.as_view(),
        name="unlike-post"
    ),

    # path(
    #     "analitics/",
    #     AnalyticsView.as_view(),
    #     name="analytics"
    # ),
]

app_name = "post"
