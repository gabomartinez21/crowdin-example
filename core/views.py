from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils.translation import gettext as _

def home(request):
    return HttpResponse(_("Hello from Django + Crowdin"))