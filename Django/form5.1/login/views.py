
# Create your views here.
from django.shortcuts import render
from .forms import LoginForm

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request, "login/form.html", {"form": form, "data": form.cleaned_data})
    else:
        form = LoginForm()

    return render(request, "login/form.html", {"form": form})

    
def thank_you(request):
    return(request,"login/thank_you.html")