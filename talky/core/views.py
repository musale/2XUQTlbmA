"""Render the templates."""
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render

User = get_user_model()


@login_required(login_url='/log_in/')
def user_list(request):
    """Render the user list template."""
    users = User.objects.select_related('logged_in_user')
    for user in users:
        user.status = 'Online' if hasattr(
            user, 'logged_in_user') else 'Offline'
    return render(request, 'core/user_list.html', {'users': users})


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


@login_required(login_url='/log_in/')
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
