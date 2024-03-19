from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect('credit:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")
                return redirect('credit:register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=firstname,
                                                last_name=lastname, email=email)

                user.save();
                messages.success(request, "* Your registration was suspenseful. Now, please sign in to continue.")
                return redirect('credit:login')
        else:
            messages.info(request, "password no match")
            return redirect('credit:register')

    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credit")
            return redirect('credit:login')

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def update_profile(request):
    user = request.user

    if request.method == 'POST':
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.set_password(request.POST['password'])
        user.save()
        update_session_auth_hash(request, user)
        return redirect('/')

    user_form = UserChangeForm(instance=user)

    context = {
            'user_form': user_form,
        }
    return render(request, 'update_profile.html', context)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')


@login_required
def delete_account(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        auth.logout(request)
        return redirect('/')
    return render(request, 'delete_account.html')


