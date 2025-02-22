from django.urls import path
from .views import register_user, login_user, user_profile, change_password, delete_user

# urlpatterns = [
#     path('register/', register_user, name='register'),
#     path('login/', login_user, name='login'),
#     path('profile/', get_user_profile, name='profile'),
# ]

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('profile/', user_profile, name='profile'),  # Updated to allow PUT
    path('change-password/', change_password, name='change-password'),  
    path('delete-account/', delete_user, name='delete-account'),
]