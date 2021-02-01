from django.urls import path

from .views import signup, update_profile

urlpatterns = [
    path('signup', signup, name='signup'),
    path('profile', update_profile, name='profile')
]
