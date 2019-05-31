from django.http import HttpResponseRedirect
from django.shortcuts import render


def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/account/login')
    return HttpResponseRedirect('/profile/')








