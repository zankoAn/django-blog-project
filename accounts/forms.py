from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        label="username",
        label_suffix="",
        error_messages={"required":"please enter the username or email"},
        widget=forms.TextInput(
            attrs={"class":"form-style", "placeholder":"user name / email", "autocomplete":"on", "type":"text"}
        )
    )

    password = forms.CharField(
        max_length=30,
        label="password",
        label_suffix="",
        error_messages={"required":"please enter the password"},
        widget=forms.PasswordInput(
            attrs={"class":"form-style", "placeholder":"password", "autocomplete":"off", "type":"password"}
        )
    )


class UserSignUpForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        label="username",
        label_suffix="",
        error_messages={"required":"please enter the username or email"},
        widget=forms.TextInput(
            attrs={"class":"form-style", "placeholder":"Username", "autocomplete":"on", "type":"text"}
        )
    )

    email = forms.EmailField(
		max_length=30,
		label="Email",
		label_suffix="",
		error_messages={"required":"Please Enter The Email"},
		widget=forms.TextInput(
			attrs={"class":"form-style", "placeholder":"Email", "autocomplete":"on", "type":"text"}
		)
	)
    
    password = forms.CharField(
        max_length=30,
        label="Password",
        label_suffix="",
        error_messages={"required":"Please enter the password"},
        widget=forms.PasswordInput(
            attrs={"class":"form-style", "placeholder":"password", "autocomplete":"off", "type":"password"}
        )
    )

    confirm_password = forms.CharField(
        max_length=30,
        label="Confirm password",
        label_suffix="",
        error_messages={"required":"Please Enter The Password to Confirmation"},
        widget=forms.PasswordInput(
            attrs={"class":"form-style", "placeholder":"Confirm password", "autocomplete":"off", "type":"password"}
        )
    )

    def clean(self):
    
        # TODO: Add better validation for password and email
        
        data = super().clean()

        password, confirm_password = data.get("password"), data.get("confirm_password")
        username, email = data.get("username"), data.get("email")
        
        errors = (
            f"User {username} already exists", 
            "This Email has already been used by another account",
            "The two password fields did't match",
            "This password is too short. It must contain at least 6 characters."
        )

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError({"username": errors[0]})
        
        elif User.objects.filter(email=email).exists():
            raise forms.ValidationError({"email": errors[1]})

        elif password != confirm_password:
            raise forms.ValidationError({"password": errors[2], "confirm_password": errors[2]})
        
        elif password and len(password) < 6:
            raise forms.ValidationError({"password": errors[3], "confirm_password": errors[3]})

        else:
            return data

