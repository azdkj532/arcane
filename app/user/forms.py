from django import forms

class LoginForm(forms.Form):
    password = forms.CharField(label="勇者密碼", widget=forms.PasswordInput(), help_text="應該會在識別證的前後左右 :)")
