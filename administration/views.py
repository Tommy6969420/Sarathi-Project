from django.shortcuts import render
from.models import Teacher
from.forms import StudentForm
# Create your views here.
def index(request):
    teachers=Teacher.objects.all()[:5]
    context={
        'teachers':teachers
    }
    return render(request,'administration/index.html',context)
def admission(request):
    if request.method=='post':
        form= StudentForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        context={
"message":"Form is submitted you may be contacted anytime soon, If you donot recieve call within 5 days, contact school administration"
        }
        return render(request,'administration/admission.html',context)
    form=StudentForm()
    context={
'form':form

    }
    return render(request,'administration/admission.html',context)