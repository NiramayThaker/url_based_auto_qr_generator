from django.shortcuts import render, redirect, HttpResponse
from .models import UserInfo
from .forms import UserInfoForm
import qrcode


def home(request):
    form = UserInfoForm()

    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            print(f"\n\n\n\n\n {request.user.id}\n\n\n\n\n")
            generate_qr(request.user.id, request.user)
            form.save()

            return redirect('home')

    context = {'form': form}
    return render(request, "form.html", context=context)


def generate_qr(id, username):
	img = qrcode.make(f"http://127.0.0.1:8000/user/{id}")
	img.save(f"./QRs/{username}.jpg")


def user_info(request, pk):
    user_info = UserInfo.objects.get(id=1)
    # user_info = "x"
    
    # context = {"user_info": user_info}
    # return render('request', 'user.html')

    return HttpResponse(pk)
