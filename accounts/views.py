from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class SignUpPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("account_login")
    template_name = "account/signup.html"