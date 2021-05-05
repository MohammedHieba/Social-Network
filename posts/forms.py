from .models import Post
from django.forms import Textarea

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)
        widgets = {
            'content':forms.Textarea(attrs={'class':'form-control'}),
        }