from django.shortcuts import render, redirect
from .forms import UserForm

def login_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('/thank_you') 
    else:
        form = UserForm()

    return render(request, "login/form.html", {"form": form})

def thank_you(request):
    return render(request, "login/thank_you.html")