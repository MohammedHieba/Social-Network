from sys import maxsize

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import PasswordInput, EmailInput, inlineformset_factory

from profile_info.models import Profile, Document


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', )
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class EditPassForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('password1', 'password2')


class DateInput(forms.DateInput):
    input_type = 'date'


class ProfileImage(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileImage, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control p-1'

    class Meta:
        model = Profile
        fields = ('profile_image',)
        exclude = ['user']


class ProfileForm(forms.ModelForm):
    # date_of_birth = forms.DateField(widget=DateInput)
    # profile_image = forms.ImageField(required=False, help_text='Optional.')

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
