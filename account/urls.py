from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordResetForm,MySetPasswordForm,MyPasswordChangeForm

urlpatterns = [
    path('registration/',views.CustomerRegistrationView.as_view(), name='registration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='myapp/login.html',
        authentication_form=LoginForm), name='login'),
    
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='myapp/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='myapp/passwordchange.html',
        form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='myapp/passwordchangedone.html'), name='passwordchangedone'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='myapp/password_reset_done.html'), name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='myapp/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='myapp/password_reset_complete.html'), name='password_reset_complete'),
    
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
]
