from django.shortcuts import render,redirect
from app.models import Student
# Create your views here.
def wonder(request):
    data=Student.objects.all()
    context={"data":data}
    return render(request,"home.html",context)
def second(request):
    return render(request,"demo.html")
def insertdata(request):
    if request.method=="POST":
        name=request.POST.get('name')
        number=request.POST.get('number')
        mail=request.POST.get('mail')
        age=request.POST.get('age')
        query=Student(Name=name,Register_Number=number,Mail_id=mail,Age=age)
        query.save()
        return redirect("/")
    return render(request,"home.html")

def updatedata(request,id):
    x=Student.objects.get(id=id)
    context={"x":x}
    
    if request.method=="POST":
        name=request.POST.get('name')
        number=request.POST.get('number')
        mail=request.POST.get('mail')
        age=request.POST.get('age')

        edit=Student.objects.get(id=id)
        edit.Name=name
        edit.Mail_id=mail
        edit.Register_Number=number
        edit.Age=age
        edit.save()
        
        return redirect("/")
    return render(request,"edit.html",context)




def deletedata(request,id):
    x=Student.objects.get(id=id)
    x.delete()
    return redirect("/")