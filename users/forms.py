from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    height = forms.FloatField(label="Altura (m)", required=False, min_value=0.3, max_value=3.0)
    weight = forms.FloatField(label="Peso (kg)", required=False, min_value=1, max_value=500)
    gender = forms.ChoiceField(label="Gênero", choices=CustomUser.GENDER_CHOICES, widget=forms.RadioSelect, required=False)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'height', 'weight', 'gender', 'password1', 'password2', 'date_of_birth']

    # deixando o erro de email ja utilizado mais amigavel 
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso. Escolha outro.")
        return email

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
