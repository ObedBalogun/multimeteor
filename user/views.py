from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RegistrationForm, UserAuthenticationForm, UserUpdateForm
from django.contrib.auth import login, authenticate, logout


# Create your views here.

def registration_view(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.save()
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('media:homepage')
        # invalid form
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'user/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('media:login')


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('media:homepage')

    #   if user isn't authenticated
    if request.POST:
        #   sets form with post data
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            #   then authenticate
            user = authenticate(email=email, password=password)

            #   authentication was successful and user object exists
            if user:
                login(request, user)
                return redirect('media:homepage')
        else:
            context['login_form'] = form

    else:
        form = UserAuthenticationForm()
        context['login_form'] = form
    return render(request, 'user/login.html', context)


def account_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {}
    if request.method == 'POST':
        form = UserUpdateForm(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            # form.picture = request.FILES['picture']
            form.save()
            return redirect("media:homepage")
    else:
        form = UserUpdateForm(
                initial={
                    "email": request.user.email,
                    "username": request.user.username,
                }
            )

    context['account_form'] = form
    return render(request, 'media/new.html', context)
