from django.urls import path
from .views import PostView

urlpatterns = [
    path("", PostView.as_view(), name="post_get"),
    path("<int:id>/", PostView.as_view(), name="post_delete"),
    path("", PostView.as_view(), name="post_post"),
    path("<int:id>/", PostView.as_view(), name="post_patch")
]