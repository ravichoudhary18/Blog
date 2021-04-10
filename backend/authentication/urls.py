from django.urls import path
from .views import RegistrationView
from django.contrib.auth.views import LoginView, LogoutView,PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeDoneView

urlpatterns = [
    path("signup/", RegistrationView.as_view(), name="signup"),
    path("login/", LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path("logout/", LogoutView.as_view(template_name='home.html'), name="logout"),
    path('password-reset/',
        PasswordResetView.as_view(
            template_name='registration/password_reset.html'
        ),
        name='password_reset'),
    path('password-reset/done/',
        PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ),
        name='password_reset_confirm'),
    path('password-reset-complete/',
        PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ),
        name='password_reset_complete'),

    path('change-password/',
        PasswordChangeView.as_view(
            template_name='registration/change-password.html'
        ),
        name='change-password'),

    path('change-password-done/',
        PasswordChangeDoneView.as_view(
            template_name='registration/change-password-done.html'
        ),
        name='password_change_done'),
    
]