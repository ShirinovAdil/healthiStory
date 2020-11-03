from .models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Citizen ID'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password',
               'id': 'passwordlogin'}))


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        widgets = {
            'angina_or_heart_attack': forms.RadioSelect,
            'menopause': forms.RadioSelect,
            'kidney_disease': forms.RadioSelect,
            'atrial_fibrillation': forms.RadioSelect,
            'pressure_treatment': forms.RadioSelect,
            'rheumatoid_arthritis': forms.RadioSelect,
            'password': forms.PasswordInput,
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
        }
        fields = [
            'name', 'surname', 'birthdate', 'email', 'phone', 'passport',
            'password', 'language', 'gender', 'height', 'blood_group',
            'country', 'city', 'physical_activity', 'smoking', 'diabets',
            'ethnicity', 'angina_or_heart_attack', 'menopause', 'kidney_disease',
            'atrial_fibrillation', 'pressure_treatment', 'rheumatoid_arthritis',
            'district', 'town'
        ]


    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        passport = cleaned_data.get('passport')
        if password != confirm_password:
            raise forms.ValidationError(
                "Your passwords do not match"
            )
        if email is None and phone is None and passport is None:
            raise forms.ValidationError(
                "You have to enter at least one of EMAIL, PHONE, Citizen ID fields"
            )

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

