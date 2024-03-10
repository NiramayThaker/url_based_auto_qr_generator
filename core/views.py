from django.shortcuts import render, redirect
from .forms import UserInfoForm

def home(request):
    form = UserInfoForm()

    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, "form.html", context=context)
