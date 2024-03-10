from django.shortcuts import render, redirect, HttpResponse
from .models import UserInfo
from .forms import UserInfoForm
import qrcode


def home(request):
    form = UserInfoForm()
    id = UserInfo.objects.values_list('user_id', flat=True)[1]
    print(f"\n\n\n\n {id} \n\n\n\n")

    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            generate_qr(id, request.user)

            return redirect('home')

    context = {'form': form}
    return render(request, "form.html", context=context)


def generate_qr(id, username):
	img = qrcode.make(f"http://127.0.0.1:8000/user/{id}")
	img.save(f"./QRs/{username}.jpg")


def user_info(request, pk):
    user_info = UserInfo.objects.get(id=pk)

    context = {'user_info': user_info}
    return render(request, 'user.html', context=context)
