"""Render the templates."""
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render


def user_list(request):
    """Render the user list template."""
    return render(request, 'core/user_list.html')


def log_in(request):
    """Authenticate a user for login."""
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('core:user_list'))
        else:
            print(form.errors)
    return render(request, 'core/login.html', {'form': form})


def log_out(request):
    """Log out a user."""
    logout(request)
    return redirect(reverse('core:log_in'))


def sign_up(request):
    """Create a new user."""
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('core:log_in'))
        else:
            print(form.errors)
    return render(request, 'core/signup.html', {'form': form})
