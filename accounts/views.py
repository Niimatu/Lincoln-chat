from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import s1
from django.views.generic import CreateView

# Create your views here.

# class Signup(CreateView):
#     form_class = s1
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'


# class Signup(CreateView):
# 	form_class = UserCreationForm
# 	success_url = reverse_lazy('accounts:login')
# 	template_name = 'accounts/signup.html'
