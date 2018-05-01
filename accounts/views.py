from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import EditProfileForm
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
# # Create your views here.
# def accounts_home(request):
#     numbers = [1,2,3,4,5]
#     name = "Nenad Pavlovic"
#
#     args = {'myName':name, 'brojevi':numbers}
#     return render(request, "accounts/login.html", args)
#

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("/")
        else:
            return render(request, 'accounts/signup.html')

            # template_name = 'accounts/signup.html'

    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'accounts/signup.html', args)



def loginview(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)

            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'The Username and Password didn\'t match'})
    else:
        return render(request, 'accounts/login.html')


def user_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)



def edit_profile(request):
    if request.method == "POST":
        form=EditProfileForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/accounts/profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })
#
# def change_pass(request):
#
#     if request.method == 'POST':
#         form = PasswordChangeForm(data=request.POST, user=request.user)
#         if form.is_valid:
#             form.save()
#             return redirect('/accounts/profile')
#     else:
#         form = PasswordChangeForm(user=request.user)
#         args = {'form': form}
#         return render(request, 'accounts/changepass.html', args)

#
# #
# # # Create your views here.
# class SignUp(CreateView):
#     from_class = UserCreationForm()
#     success_url = reverse_lazy('login')
#     template_name = 'accounts/signup.html'
