from django.contrib.auth.models import User
from django import forms
from .models import Group


class CreateGroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateGroupForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control p-1'

    owner = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Group
        fields = '__all__'
        exclude = ('created_at', 'members')


class EditGroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditGroupForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control p-1'

    owner = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Group
        fields = '__all__'
        exclude = ('created_at', 'members', 'group_image')


class EditGroupImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditGroupImageForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control p-1'

    class Meta:
        model = Group
        fields = '__all__'
        exclude = ('created_at', 'members', 'owner', 'name', 'description')
