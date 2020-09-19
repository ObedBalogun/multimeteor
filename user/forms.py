from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import UserAccount


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    #   Meta is just extra data about the aforementioned 'model'
    class Meta:
        model = UserAccount
        fields = ('email', 'username', 'password1', 'password2',)
        # password1 and password2 are required by the UserCreationForm class


#   Creating(with forms.ModelForm)  custom User Authentication form

class UserAuthenticationForm(forms.ModelForm):
    #    hides password
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = UserAccount
        fields = ('email', 'password')

    #   available to any form that extends ModelForm. This code runs before form can do anything
    def clean(self):
        #   if form(self) is valid
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                #   if you can't authenticate provided parameters
                raise forms.ValidationError("Invalid Login")


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('email', 'username', 'picture',)

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                #   get all accounts excluding the one entered by the user
                account = UserAccount.objects.exclude(pk=self.instance.pk).get(email=email)
            except UserAccount.DoesNotExist:
                return email
            raise forms.ValidationError("Email '%s' is already in use" % account)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                #   get all accounts excluding the one entered by the user
                account = UserAccount.objects.exclude(pk=self.instance.pk).get(username=username)
            except UserAccount.DoesNotExist:
                return username
            raise forms.ValidationError("Username '%s' is already in use" % username)

    # def clean_picture(self):
    #     print('Hitting')
    #     if self.is_valid():
    #         print("Valid")
    #         picture = self.cleaned_data['picture']
    #         if picture:
    #             return picture
    #     else:
    #         print('Invalud')
