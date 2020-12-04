from django.urls import path
from reports_auth.views import login_user, logout_user, RegisterView


urlpatterns = (
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('register/', RegisterView.as_view(), name='register user')
    #path('register/', register_user, name='register user')
)