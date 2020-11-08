from django.urls import path

from user import views

urlpatterns = [
    path('user-signup/', views.UserSignup.as_view(), name='user_signup'),
    path('user-login/', views.UserSignIn.as_view(), name='user_login'),
    path('profile-details/<int:user_id>/', views.UserSignIn.as_view(), name='get_profile_details'),

]
