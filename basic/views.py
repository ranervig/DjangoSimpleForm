from django.shortcuts import render
from django.shortcuts import redirect
from basic.forms import StudentForm
from basic.models import Student
from django.views.generic import ListView

def home(request):
    form= StudentForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect("result")
    else:
        return render(request,'basic/home.html',{"form": form})

class Result(ListView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(Result,self).get_context_data(**kwargs)
        return context
    