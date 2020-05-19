from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from .models import Profile

class UserSignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

'''Детализация профиля'''
def profile_detail(request, pk):
    profile = Profile.objects.get(pk=pk)
