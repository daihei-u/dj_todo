#from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import TemplateView

from .forms import SignUpForm,activate_user


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
# Create your views here.

class ActivateView(TemplateView):
    template_name = "registration/activate.html"

    def get(self, request, uidb64, token, *args, **kwargs):
        result = activate_user(uidb64, token)
        return super().get(request, result=result, **kwargs)
