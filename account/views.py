from lib2to3.fixes.fix_input import context

from django.contrib.auth import logout
from django.shortcuts import render, redirect

from account.forms import UserRegistrationForm


# Create your views here.
def user_logout(request):
    logout(request)
    return redirect('login')


def dashboard_view(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'account/profile.html', context=context)

def user_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        new_user = user_form.save(commit=False)
        new_user.set_password(
            user_form.cleaned_data['password']
        )
        new_user.save()
        context = {
            'user_form': user_form
        }

        return render(request, 'account/register.html', context)