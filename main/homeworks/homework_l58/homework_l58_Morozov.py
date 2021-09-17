from django.forms import ModelForm, TextInput, EmailInput

from .models import PostModel

class PostForm(ModelForm):
    class Meta:
        model = PostModel
        fields = ('login', 'email', 'nickname')
        widgets = {
            'login': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин',
                'id': 'floatingLogin',
                'autocomplete': 'off',
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Электронная почта',
                'id': 'floatingEmail',
            }),
            'nickname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Игровое имя',
                'id': 'floatingNickname',
            }),
        }
