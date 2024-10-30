

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import  path

from account.views import user_logout, dashboard_view, user_register

urlpatterns = [
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', user_logout, name='logout'),

    path('profile/', dashboard_view, name= 'profile'),

    path('password_change/', PasswordChangeView.as_view(), name = 'password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', PasswordResetView.as_view(), name= 'password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('signup/', user_register, name= 'signup')
]