from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = get_user_model()
        fields = ['email', 'username','password']

    class RegisterForm(forms.Form):
          email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))