from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views
app_name='accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reset/', auth_views.password_reset,
         {'template_name': 'accounts/password_reset_form.html',
          'email_template_name': 'accounts/password_reset_email.html',
          'subject_template_name': 'accounts/password_reset_subject.txt',
          'post_reset_redirect': 'accounts:password_reset_done'},
    name='password_reset'),
    path('reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
        path('reset/<uidb64>/<token>/', auth_views.password_reset_confirm,
         {'template_name': 'accounts/password_reset_confirm.html',
          'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),
    path('reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    path('settings/password/change/', auth_views.password_change,{'template_name': 'accounts/password_change.html', 'post_change_redirect': 'accounts:password_change_done'}, name='password_change' ),
    path('settings/password/change/done', auth_views.password_change_done, {'template_name': 'accounts/password_change_done.html'}, name='password_change_done'),
    path('settings/account/', views.UserUpdateView.as_view(), name='my_account')
    ]
