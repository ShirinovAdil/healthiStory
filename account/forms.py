from .models import User, Country, City, District
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
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label=None)
    district = forms.ModelChoiceField(queryset=District.objects.all(), empty_label=None)
    city = forms.ModelChoiceField(queryset=None, empty_label=None)
    city2 = forms.CharField(max_length=255, label="City")

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
        if self.cleaned_data['country'] == 1:
            user.city = self.cleaned_data["city"]
        else:
            user.city = self.cleaned_data["city2"]

        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
        self.fields['district'].queryset = District.objects.none()

        if 'country' in self.data:
            try:
                self.fields['city'].queryset = City.objects.filter(country=1)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')

        if 'district' in self.data:
            try:
                city_id = int(self.data.get('city_id'))
                self.fields['district'].queryset = District.objects.filter(city=city_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.city.district_set.order_by('name')

