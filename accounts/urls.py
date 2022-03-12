from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from .views import sign_up_view,after_login

urlpatterns = [
    
    path('signup/',sign_up_view,name='sign_up'),
    path('login/', LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout',LogoutView.as_view(template_name="accounts/logout.html"),name='logout'),
    path('password_reset/',PasswordResetView.as_view(template_name="accounts/password_reset_form.html"),name='password_reset'),
    path('password_reset/done/',PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
    name='password_reset_complete'),


    





    path('afterloggin/',after_login, name= 'after_loggin')
]
