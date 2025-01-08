from django.urls import path
from .views import CareerView

urlpatterns = [
    path("", CareerView.as_view(), name="career_get"),
    path("<int:id>/", CareerView.as_view(), name="career_delete")
]