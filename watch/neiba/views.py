from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegistrationForm,ProfileEditForm,UserEditForm,NewPostForm,NewHoodForm
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
    # post = Post.objects.all()
    # public = Social.objects.all()
    # return render(request, 'home.html', {"post": post, "public": public})
    return render(request, 'home.html')

@login_required
def Profile(request):
    '''
    This is a view function to show the profile details and details of the user
    '''
    return render(request,'profile/profile.html')

@login_required
def edit(request):
     current_user = request.user

     if request.method == 'POST':
        if Profile.objects.filter(user_id= current_user):

            profile_form = ProfileEditForm(request.POST,request.FILES,instance = Profile.objects.get(user_id=current_user))
        else:
            profile_form = ProfileEditForm(request.POST,request.FILES)

        if profile_form.is_valid():
            userProfile=profile_form.save(commit = False)
            userProfile.user = current_user
            userProfile.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
     else:

        profile_form = ProfileEditForm()
     return render(request, 'profile/profile.html', {'profile_form': profile_form})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('home')
    else:
        form = NewPostForm()
    return render(request, 'neiba/post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def neighbourhood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewHoodForm(request.POST)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = current_user
            hood.save()
            return redirect('home')
    else:
        form = NewHoodForm()
    return render(request, 'neiba/neibahood.html', {"form": form})


@login_required(login_url='/accounts/login/')
def neibadisplay(request):
    hoods = NeighbourHood.objects.all()
    return render(request, 'allneibas.html', {"hoods": hoods})

def join(request, hoodId):
    '''
    This view function will enable new users join a given neighbourhood
    '''
    neighbourhood = NeighbourHood.objects.get(pk=hoodId)
    if Join.objects.filter(user_id=request.user).exists():
        messages.success(
            request, 'Welcome. You are now a member of this Neighbourhood')
        Join.objects.filter(user_id=request.user).update(hood_id=neighbourhood)
        return redirect('displayhood')
    else:
        messages.success(
            request, 'Welcome. You are now a member of this Neighbourhood')
        Join(user_id=request.user, hood_id=neighbourhood).save()
        return redirect('displayhood')
