from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm, MyPasswordResetForm, MySetPasswordForm
from .views import MyPasswordResetView

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',
                                                authentication_form=LoginForm),
         name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),

    # Password Reset URLs
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='core/password_reset_form.html',
             form_class=MyPasswordResetForm,
             success_url=reverse_lazy('core:password_reset_done'),
             email_template_name='core/password_reset_email.html',
             subject_template_name='core/password_reset_subject.txt'
         ),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='core/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='core/password_reset_confirm.html',
             form_class=MySetPasswordForm,
             success_url=reverse_lazy('core:password_reset_complete')
         ),
         name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='core/password_reset_complete.html'),
         name='password_reset_complete'),
]
