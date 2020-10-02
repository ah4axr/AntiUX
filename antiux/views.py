from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.db import connection
from django.http import HttpResponse

from .models import User
from .forms import UserForm

class IndexView(generic.CreateView):
    template_name = 'antiux/index.html'
    success_url = reverse_lazy('antiux:index')
    form_class = UserForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return super(IndexView, self).form_valid(form)
        

class PasswordView(generic.CreateView):
    template_name = 'antiux/password.html'
    success_url = reverse_lazy('antiux:password')
    form_class = UserForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return super(PasswordView, self).form_valid(form)

class ResultsView(generic.CreateView):
    template_name = 'antiux/results.html'
    success_url = reverse_lazy('antiux:results')
    form_class = UserForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return super(ResultsView, self).form_valid(form)

class GuitarUsernameView(generic.CreateView):
    template_name = 'antiux/guitarUsername.html'
    success_url = reverse_lazy('antiux:guitarUsername')
    form_class = UserForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return super(GuitarUsernameView, self).form_valid(form)

class GuitarView(generic.CreateView):
    template_name = 'antiux/guitar.html'
    success_url = reverse_lazy('antiux:guitar')
    form_class = UserForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return super(GuitarView, self).form_valid(form)

class DrumsUsernameView(generic.CreateView):
    template_name = 'antiux/drumsUsername.html'
    success_url = reverse_lazy('antiux:drumsUsername')
    form_class = UserForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return super(DrumsUsernameView, self).form_valid(form)

class DrumsView(generic.CreateView):
    template_name = 'antiux/drums.html'
    success_url = reverse_lazy('antiux:drums')
    form_class = UserForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return super(DrumsView, self).form_valid(form)

class PianoUsernameView(generic.CreateView):
    template_name = 'antiux/pianoUsername.html'
    success_url = reverse_lazy('antiux:pianoUsername')
    form_class = UserForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return super(PianoUsernameView, self).form_valid(form)

class PianoView(generic.CreateView):
    template_name = 'antiux/piano.html'
    success_url = reverse_lazy('antiux:piano')
    form_class = UserForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return super(PianoView, self).form_valid(form)

class BassUsernameView(generic.CreateView):
    template_name = 'antiux/bassUsername.html'
    success_url = reverse_lazy('antiux:bassUsername')
    form_class = UserForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return super(BassUsernameView, self).form_valid(form)

class BassView(generic.CreateView):
    template_name = 'antiux/bass.html'
    success_url = reverse_lazy('antiux:bass')
    form_class = UserForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return super(BassView, self).form_valid(form)