from django.shortcuts import  redirect
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import FormView 


from .forms import UserLoginForm, UserSignUpForm


@method_decorator(login_required, name="dispatch")
class LogoutUserView(LogoutView):
    def get(self, request, *args, **kwargs):
        user = request.user
        messages.success(request, "you have successfully logged out", "success")
        return redirect("Posts:home-page")


class LoginUserView(FormView):
    template_name = "accounts/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy("Posts:home-page")
    extra_context = {"request_to" : "Login"}

    def form_valid(self, form):
        data = form.cleaned_data
        user = authenticate(username=data.get("username"), password=data.get("password"))

        if user is None:
            messages.error(self.request, "Username or password is worrng!!", "danger")
            return redirect("Account:login")

        else:
            login(self.request, user)
            messages.success(self.request, "You Are Successfully Login in", "success")
            return super().form_valid(form)



class SignUpUserView(FormView):
    template_name = "accounts/login.html"
    form_class = UserSignUpForm
    success_url = reverse_lazy("Posts:home-page")
    extra_context = {"request_to" : "SignUp"}
    
    def form_valid(self, form):
        data = form.cleaned_data
        User.objects.create_user(data["username"], data["email"], data["password"]) 
        user = User.objects.get(username=data["username"])
        login(self.request, user)

        messages.success(self.request, f"The {data['username']} user was successfully registered", "success")
        return super().form_valid(form)



