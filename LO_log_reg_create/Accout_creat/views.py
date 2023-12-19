from django.shortcuts import render, redirect # 
from .forms import RegisterForm, ChangeUserData # changeUserData inherite 
from django.contrib import messages # jokon user login/logout korve 
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm # old password diye
# new password diye set 
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash # built in login logout and password update korar 
# built in update_session_auth_hash
# Create your views here.


def home(request):
    return render(request, './home.html')


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Logged in successfully')
                form.save()
                print(form.cleaned_data)
        else:
            form = RegisterForm()
        return render(request, './signup.html', {'form': form})
    else:
        return redirect('profile')

def user_logout(request):
    # if  request.user.is_authenticated:
    #     if request.method == 'POST':
    #         form = RegisterForm(request.POST)
    #         if form.is_valid():
    #             logout(request)
    #             messages.success(request, 'Logout in successfully')
    #             print(form.cleaned_data)
    #             return redirect('login')
    #     else:
    #         form = RegisterForm()
    #     return render(request, './signup.html', {'form': form})
 
        
    logout(request)
    # print("Logout successful")
    messages.success(request, 'Logout  successfully')
    return redirect('login')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            # check kortechi user database e ache kina
            user = authenticate(username=name, password=userpass)
            if user is not None:
                login(request, user)
                return redirect('profile')  # profile page e redirect korbe
            
    else:
        form = AuthenticationForm() #user jodi kico pass nah kore 
    return render(request, './login.html', {'form': form})


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
        else:
            form = ChangeUserData(instance=request.user)
        return render(request, './profile.html', {'form': form})
    else:
        return redirect('signup')





def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # password update korbe
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, './pass_cng.html', {'form': form})
    else:
        return redirect('login')


def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # password update korbe
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, './pass_cng.html', {'form': form})
    else:
        return redirect('login')


def change_user_data(request):
    if request.user.is_authenticated: # user jodi valid hoy tahole profile bah tar data gulu update korte parve
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
                print(form.cleaned_data)
        else:
            form = ChangeUserData(instance=request.use)
        return render(request, './profile.html', {'form': form})
    else:
        return redirect('signup')