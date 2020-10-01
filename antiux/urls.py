from django.urls import path

from . import views

app_name = 'antiux'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('password/', views.PasswordView.as_view(), name='password'),
    path('results/', views.ResultsView.as_view(), name='results'),
]