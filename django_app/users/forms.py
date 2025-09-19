from django import forms
from .models import User


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Подтверждение пароля'
    )

    class Meta:
        model = User
        fields = ['login', 'email', 'password']
        widgets = {
            'login': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'login': 'Логин',
            'email': 'Email',
            'password': 'Пароль',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email уже зарегистрирован")
        return email

    def clean_login(self):
        login = self.cleaned_data.get('login')
        if User.objects.filter(login=login).exists():
            raise forms.ValidationError("Логин уже занят")
        return login