from django.urls import path

from . import views

app_name = "middleware_example"

urlpatterns = [
    path("example-1", views.Example1View.as_view(), name="example_1"),
    path("example-2", views.Example2View.as_view(), name="example_2"),
]
