# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Application, Competition

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'CIN', 'address', 'date_of_birth', 'place_of_birth', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            self.add_error('username', 'Username already exists')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'etudiant'
        if commit:
            user.save()
        return user

class SignInForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'CIN', 'address', 'phone', 'date_of_birth', 'place_of_birth')

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('competition', 'baccalaureate_category','baccalaureate_grade', 'diploma_category', 'diploma_year', 'diploma_grade', 'language')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['competition'].queryset = Competition.objects.all()

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ('type', 'field', 'deadline')