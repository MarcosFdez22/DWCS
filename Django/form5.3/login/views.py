from django.shortcuts import render, redirect
from .forms import UserForm
from django.http import HttpResponseRedirect
from django.views import View

class LoginView(View):
    def get(self,request):
        form = UserForm()

        return render(request, "login/form.html",{
            "form":form
        })
    def post(self,request):
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank_you")
        
        return render(request, "login/form.html", {
            "form": form
        })

def thank_you(request):
    return render(request, "login/thank_you.html")