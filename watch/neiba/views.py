from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegistrationForm,
from django.contrib import messages

# Create your views here.
