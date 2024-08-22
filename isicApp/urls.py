from django.urls import path
from . import views
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('res-dash/', views.res_dash, name='res-dash'),
    path('edu-dash/', views.user_profile, name='edu-dash'),
    path('res-dash/', views.user_profile, name='res-dash'),
    path('export-excel/', views.export_excel, name='export_excel'),
    path('export-pdf/', views.export_pdf, name='export_pdf'),
    path('sign-out/', views.sign_out, name='sign-out'),
    path('profile/', views.profile_view, name='profile'),
    path('application-details/<int:application_id>/', views.application_details_view, name='application_details'),
    path('applications/', views.view_application, name='applications'),
    path('edit-application/<int:application_id>/', views.edit_application, name='edit_application'),
    path('view_app/<int:application_id>/', views.view_app, name='view_app'),
    path('add-competition/', views.add_competition, name='add-competition'),
    path('api/add-competition/', views.api_add_competition, name='api_add_competition'),
    path('api/competitions/', views.get_competitions, name='api_competitions'),
    path('api/application-stats/', views.get_application_stats, name='api_application_stats'),
    path('overview/', views.overview, name='overview'),
    path('api/latest-competitions/', views.latest_competitions, name='latest_competitions'),
    path('add-application/<int:competition_id>/', views.add_application, name='add_application'),
    path('get-user-info/', views.get_user_info, name='get_user_info'),
    path('submit-general-application/', views.submit_general_application, name='submit-general-application'),
    path('my-apps/', views.my_apps_view, name='my_apps'),
    path('api/user-applications/', views.user_applications, name='user_applications'),
    path('api/application-details/<int:application_id>/', views.application_details, name='application_details'),
    path('api/update-application/<int:application_id>/', views.update_application, name='update_application'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('api/latest-applications/', views.latest_applications, name='latest-applications'),
    path('notifications-res/', views.notifications_res_view, name='notifications-res'),

    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html',html_email_template_name='users/password_reset_email.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
]