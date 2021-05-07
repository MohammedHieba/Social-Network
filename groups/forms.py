from accounts.models import User
from django import forms

from posts.models import Post
from .models import Group


class CreateGroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateGroupForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control p-1'

    owner = forms.ModelChoiceField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), queryset=User.objects.all())

    class Meta:
        model = Group
        fields = '__all__'
        exclude = ('created_at', 'members')


class EditGroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditGroupForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control p-1'

    owner = forms.ModelChoiceField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), queryset=User.objects.all())

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


class PostGroupForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': '3', 'placeholder': 'Say Something...'}))

    def __init__(self, *args, **kwargs):
        super(PostGroupForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control p-1'
    class Meta:
        model = Post
        fields = ['body']
