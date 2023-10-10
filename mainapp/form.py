from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinLengthValidator


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Elimina los mensajes de ayuda predeterminados
        self.fields['username'].help_text = ''
        self.fields['email'].help_text = ''
        self.fields['password1'].help_text = 'Tu contraseña debe tener al menos 8 caracteres.'
        self.fields['password2'].help_text = 'Repite tu contraseña para confirmar.'

    email = forms.EmailField(max_length=254, required=True,
                             help_text='ingresa un email valido')
    first_name = forms.CharField(label="Nombre", max_length=100)
    last_name = forms.CharField(label="Apellido", max_length=100)

    class Meta:
        model = UserCreationForm.Meta.model
        # Campos personalizados en el formulario base
        fields = ['username', "first_name", "last_name",
                  "email", "password1", "password2"]


class UserEditForm(UserCreationForm):
    first_name = forms.CharField(label="Modificar nombre")
    last_name = forms.CharField(label="Modificar apellido")
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(
        label="Contraseña", widget=forms.PasswordInput, validators=[MinLengthValidator(8)])
    password2 = forms.CharField(
        label="Repetir la contraseña", widget=forms.PasswordInput, validators=[MinLengthValidator(8)])

    class Meta:
        model = UserCreationForm.Meta.model
        fields = ["first_name", "last_name",
                  "email", "password1", "password2"]
