from django.forms import ModelForm
from .models import User


class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'name', 'surname', 'birthdate', 'email', 'phone', 'passport',
            'password', 'language', 'gender', 'height', 'blood_group',
            'country', 'city', 'physical_activity', 'smoking', 'diabets',
            'ethnicity', 'angina_or_heart_attack', 'menopause', 'kidney_disease',
            'atrial_fibrillation', 'pressure_treatment', 'rheumatoid_arthritis'
        ]

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
