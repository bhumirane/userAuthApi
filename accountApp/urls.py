from accountApp.views import UserRegistrationView, UserLoginView,UserProfileView,UserProfileChangePasswordView,SendPasswordResetEmailView,UserPasswordResetView
from django.urls import path
urlpatterns = [
   path('register/',UserRegistrationView.as_view(),name='register'),
   path('login/',UserLoginView.as_view(),name='login'),
   path('profile/',UserProfileView.as_view(),name='profile'),
   path('changepsw/',UserProfileChangePasswordView.as_view(),name='changepsw'),
   path('sendPasswordReset/',SendPasswordResetEmailView.as_view(),name='sendPasswordReset'),
   path('resetpassword/<uid>/<token>/',UserPasswordResetView.as_view(),name='resetpassword'),
   
   
   
]
