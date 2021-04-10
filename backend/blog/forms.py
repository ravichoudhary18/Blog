from django.contrib.auth.models import User
from authentication.models import Profile
from django.forms import ModelForm
from .models import Contact, Blog
from datetime import date
from django import forms

class ContectForm(ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        if not (email):
            raise forms.ValidationError("You must enter an email")


start_year = date.today().year-120
corrent_year = date.today().year-1
YEARS= [x for x in range(start_year,corrent_year)]


class ProfileUpdateForm(forms.ModelForm):
    DOB = forms.DateField(label='Date of Birth', widget=forms.SelectDateWidget(years=YEARS))

    class Meta:
        model = Profile
        fields = ['phone', 'image', 'sex','date_of_birth']

    # def clean_phone(self):
    #     phone = self.cleaned_data['phone']
    #     if not phone.isdigit():
    #         raise forms.ValidationError('Phone number can only contains digits')
    #     elif len(phone) != 10:
    #         raise forms.ValidationError('Length of phone number must be 10 digits')
    #     return phone


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'username']


class UsernameUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class AddBlogFroms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','description','image','category','body']
