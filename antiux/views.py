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
