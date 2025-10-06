from django.urls import path

from . import views

app_name = 'toys'

urlpatterns = [
    path(
        '',
        views.ToyListView.as_view(),
        name='index',
    ),
]
