from django.urls import path
from .views import home, post_data

urlpatterns = [
    path('', home, name='Home'),
    path('post-vendor/', post_data, name="Post-vendors"),
]
