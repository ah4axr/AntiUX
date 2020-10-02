from django.urls import path

from . import views

app_name = 'antiux'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('guitar/', views.GuitarView.as_view(), name='guitar'),
    path('drums/', views.DrumsView.as_view(), name='drums'),
    path('piano/', views.PianoView.as_view(), name='piano'),
    path('bass/', views.BassView.as_view(), name='bass'),
    path('guitarUsername/', views.GuitarUsernameView.as_view(), name='guitarUsername'),
    path('drumsUsername/', views.DrumsUsernameView.as_view(), name='drumsUsername'),
    path('pianoUsername/', views.PianoUsernameView.as_view(), name='pianoUsername'),
    path('bassUsername/', views.BassUsernameView.as_view(), name='bassUsername'),
    path('password/', views.PasswordView.as_view(), name='password'),
    path('results/', views.ResultsView.as_view(), name='results'),
]