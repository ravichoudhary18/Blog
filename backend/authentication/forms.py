from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','maxlength':"75",'pattern':'([a-z0-9](_)[a-z0-9])*', 'title':'Enter Characters Only '}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",'first_name','last_name')

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')


    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user



# class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
#     def _make_hash_value(self, user, timestamp):
#         return (
#             six.text_type(user.pk) + six.text_type(timestamp) +
#             six.text_type(user.profile.email_confirmed)
#         )

# account_activation_token = AccountActivationTokenGenerator()