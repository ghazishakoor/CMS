from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(
         template_name='auth/login.html'
         ), name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='auth/password_reset.html'
        ),
        name='password_reset'
    ),
    path(
        'password_reset_done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='auth/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset/confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='auth/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='auth/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            template_name='auth/password_change.html'
        ),
        name='password_change'
    ),
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='auth/password_change_done.html'
        ),
        name='password_change_done'
    ),
]
