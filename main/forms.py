from django import forms
# from tinymce import TinyMCE
from .models import Signup,Login

# class TinyMCEWidget(TinyMCE):
#     def use_required_attribute(self, *args):
#         return True

class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    last_name = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.EmailField(
        required = True,
        label = 'Email',
        max_length = 82,
        help_text="Required. Inform a valid email address"
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )

    class Meta:
        # model = User
        fields = ("first_name", "last_name", "email", "password1","password2",)

class UserRegistrationForm(forms.Form):
    email = forms.EmailField(
        required = True,
        label = 'Email',
        max_length = 82,
        help_text="Required. Inform a valid email address"
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )

 