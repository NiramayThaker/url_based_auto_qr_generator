from django.shortcuts import render, redirect, HttpResponse
from .models import UserInfo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserInfoForm, RegistrationForm
import qrcode


@login_required(login_url="login")
def home(request):
    form = UserInfoForm()
    # id = UserInfo.objects.values_list('user_id', flat=True)[0]
    # print(f"\n\n\n\n {id} \n\n\n\n")

    user_name = User.objects.get(id=request.user.id)
    print(f"\n\n\n\n\n\n\n {user_name} \n\n\n\n\n\n\n")

    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            # generate_qr(id, request.user)

            return redirect('home')

    context = {'form': form}
    return render(request, "core/form.html", context=context)


def generate_qr(id, username):
	img = qrcode.make(f"http://127.0.0.1:8000/user/{id}")
	img.save(f"./QRs/{username}.jpg")


def user_info(request, pk):
    user_info = UserInfo.objects.get(user_id=pk)

    context = {'user_info': user_info}
    return render(request, 'user.html', context=context)


def info(request):
    user_info = UserInfo.objects.get(id=1)

    context = {'user_info': user_info}
    return render(request, 'user.html', context=context)


def sign_up(reqeuest):
    form = RegistrationForm()

    context = {"form": form}
    return render(reqeuest, "registration/signup.html", context=context)
