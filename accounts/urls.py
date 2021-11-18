from django.urls import path
from .views import LogoutUserView, LoginUserView, SignUpUserView

app_name = "Account"

urlpatterns = [
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("signup/", SignUpUserView.as_view(), name="signup"),
]
