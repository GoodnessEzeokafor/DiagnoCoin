from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserCreateForm

# Create your views here.



class SignUp(CreateView):
    template_name = 'account/signup.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('home')

