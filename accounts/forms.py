from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150, label="Ім'я")
    last_name = forms.CharField(max_length=150, label="Прізвище")
    email = forms.EmailField(label='Email')

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'city', 'address']
        labels = {
            'phone_number': 'Телефон',
            'city': 'Місто',
            'address': 'Адреса',
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email

    def save(self, commit=True):
        profile = super().save(commit=False)

        if self.user:
            self.user.first_name = self.cleaned_data['first_name']
            self.user.last_name = self.cleaned_data['last_name']
            self.user.email = self.cleaned_data['email']

            if commit:
                self.user.save()

        if commit:
            profile.save()

        return profile
