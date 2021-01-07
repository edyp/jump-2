from django.urls import path

from users.views import SignUpView
# TODO: Rejestracja użytkownika wciąż pobiera dane z auth.User, napraw to.


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
