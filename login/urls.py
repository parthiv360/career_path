from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

app_name = 'login'
urlpatterns=[
    path('', views.login, name="login"),
    path('logout', views.logout, name='logout'),
    path('register',views.register, name="register"),
    path('pg1',views.pg1, name="pg1"),
    path('password/', auth_views.PasswordResetView.as_view(template_name= 'login/password-change1.html'),name="reset_password"),
    path('login/reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name= 'login/password-reset-sent.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'login/password-change.html'),name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name= 'login/password-change-done.html'),  name="password_reset_complete"),

    
]