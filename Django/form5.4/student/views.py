from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import StudentForm
from .models import Student
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
# Create your views here.
class StudentFormView(View):
    def get(self, request):
        form = StudentForm()

        return render(request,"student/studentform.html",{
            "form":form
        })
    def post(self,request):
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank_you")
        return render(request,"student/studentform.html",{
            "form":form
        })
    
def thank_you(request):
    return render(request,"student/thank_you.html")



class StudentList(ListView):
 template_name = "student/list.html"
 model = Student
 context_object_name = "students"

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'degree']
    template_name = 'student/studentupdateform.html'
    success_url = reverse_lazy('list')  

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student/student_confirm_delete.html'
    success_url = reverse_lazy('list')  