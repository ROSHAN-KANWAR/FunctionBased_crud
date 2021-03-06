from django.shortcuts import (get_object_or_404,render)
from .models import Student
from .forms import modelform
from django.http import HttpResponseRedirect



##mForm data
def MForm(request):
    if request.method=='POST':
        fm=modelform(request.POST)
        if fm.is_valid():
            fname=fm.cleaned_data['fname']
            lname=fm.cleaned_data['lname']
            email=fm.cleaned_data['email']
            city=fm.cleaned_data['city']
            fm1=Student(fname=fname,lname=lname,email=email,city=city)
            fm1.save()
            fm=modelform()
            return HttpResponseRedirect('/')
    else:
            fm=modelform()

            stu = Student.objects.all()
    return render(request,'home.html',{'fm':fm,'stu':stu})
  ##
#delete
def delete_data(request,id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        pi.delete()
    return render(request,'del.html',{'id':id})
##edit
##def edit_data(request,id):
  #  context = {}
  #  obj = get_object_or_404(Student, id=id)
  #  form = modelform(request.POST or None, instance=obj)
  #  if form.is_valid():
  #      form.save()
   #     return HttpResponseRedirect("/")
  #  context["form"] = form

   # return render(request, "edit.html", context)

def edit_data(request,id):
    if request.method=="POST":
        pi=Student.objects.get(pk=id)
        fm=modelform(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        pi=Student.objects.get(pk=id)
        fm=modelform(instance=pi)
    return render(request,'edit.html',{'fm':fm})