from django import forms

choices = [("1", "student"), ("2", "admin"), ('3', 'editor'), ('4', "staff")]


class RegisterationForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "username"}), max_length=30, min_length=3, required=True)
    role = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter role"}), required=True)
    nationality = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "nationality"}), required=True)
    country = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "country"}), required=True)
    email = forms.CharField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "email"}), required=True)
    phone = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "phone"}), required=True, max_length=10, min_length=10)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "password"}), required=True, min_length=12)


class loginUserForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control", "placeholder": "email"}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "password"}), required=True)
