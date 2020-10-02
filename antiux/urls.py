from django.urls import path

from . import views

app_name = 'antiux'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('guitarUsername/', views.GuitarUsernameView.as_view(), name='guitarUsername'),
    path('guitarPassword/', views.GuitarPasswordView.as_view(), name='guitarPassword'),
    path('guitar/', views.GuitarView.as_view(), name='guitar'),

    path('drumsUsername/', views.DrumsUsernameView.as_view(), name='drumsUsername'),
    path('drumsPassword/', views.DrumsPasswordView.as_view(), name='drumsPassword'),
    path('drums/', views.DrumsView.as_view(), name='drums'),

    path('pianoUsername/', views.PianoUsernameView.as_view(), name='pianoUsername'),
    path('pianoPassword/', views.PianoPasswordView.as_view(), name='pianoPassword'),
    path('piano/', views.PianoView.as_view(), name='piano'),

    path('bassUsername/', views.BassUsernameView.as_view(), name='bassUsername'),
    path('bassPassword/', views.BassPasswordView.as_view(), name='bassPassword'),
    path('bass/', views.BassView.as_view(), name='bass'),

    path('password/', views.PasswordView.as_view(), name='password'),
    path('results/', views.ResultsView.as_view(), name='results'),
]