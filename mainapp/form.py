from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Elimina los mensajes de ayuda predeterminados
        self.fields['username'].help_text = ''
        self.fields['email'].help_text = ''
        self.fields['password1'].help_text = 'Tu contraseña debe tener al menos 8 caracteres.'
        self.fields['password2'].help_text = 'Repite tu contraseña para confirmar.'

    email = forms.EmailField(max_length=254, required=True,
                             help_text='Required. Enter a valid email address.')

    class Meta:
        model = UserCreationForm.Meta.model
        # Campos personalizados en el formulario base
        fields = ('username', 'email', 'password1', 'password2',)
