from django.db.models import Model
from django import forms

from chats.models import Message


class MessageForm(forms.ModelForm):
    message = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'w-100 form-control mb-1',
        'autofocus': 'autofocus'
    }))

    class Meta:
        model = Message
        fields = ('message',)
