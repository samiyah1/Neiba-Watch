from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegistrationForm,ProfileEditForm
from django.contrib import messages

# Create your views here.
def user_login(request):
    """
    This a view method to allow users to login the neighbourhood app
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def register(request):
    """
    view function to create user registration form and allow users to register
    """
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():

            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user,'profile':profile})
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/registration_form.html', {'form': form})

@login_required
def home(request):
    '''
    This the home page view function and all that is in the home templates
    '''
    post = Post.objects.all()
    public = Social.objects.all()
    return render(request, 'home.html', {"post": post, "public": public})

@login_required
def Profile(request):
    '''
    This is a view function to show the profile details and details of the user
    '''
    return render(request,'profile/profile.html')
