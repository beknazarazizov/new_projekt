
from django import forms

from customer.models import Customer, User


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude =()

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=255)

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email does not exist")
        return email

    def clean_password(self):
        email = self.cleaned_data.get('email')
        user = User.objects.filter(email=email)
        password = self.data.get('password')
        if not user.check_password(password):
            raise forms.ValidationError("Password does not exist")
        return password
