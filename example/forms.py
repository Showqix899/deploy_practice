from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password']


    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user