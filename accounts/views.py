from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def register(request):
    if request.method == "POST":
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect('home')
    else:
        register_form = RegistrationForm()
    return render(request, 'accounts/register.html', {'register_form': register_form})

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'accounts/my_account.html'
    success_url = reverse_lazy('accounts:my_account')

    def get_object(self):
        return self.request.user
