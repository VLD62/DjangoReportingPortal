from django.urls import path
from reports_auth.views import LoginView, RegisterView, LogoutView


urlpatterns = (
    path('register/', RegisterView.as_view(), name='register user'),
    path('login/', LoginView.as_view(), name='login user'),
    path('logout/', LogoutView.as_view(), name='logout user'),
)