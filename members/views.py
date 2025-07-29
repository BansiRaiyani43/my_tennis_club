from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import student,subject

# Create your views here.
def demo(request):
  return HttpResponse("Hello world!")

def demo3(request):
  return HttpResponse("You are in contact us page")

def demo2(request):
  return render(request,"home.html")

def demo1(request):
  s1 = student.objects.all().order_by('firstname')
  
  context ={
    's1' : s1
  }
  print(context)
  return render(request,"firsttemplate.html",context)

#add student function start...
def add_student(request):
  if request.method =="POST":

    fname = request.POST['fname']
    lname = request.POST['lname']  
    age = request.POST['age']
    email = request.POST['email']
    phone = request.POST['phone']
    img = request.FILES['img']

    f1 = student()
    f1.firstname=fname
    f1.lastname=lname
    f1.age=age
    f1.email=email
    f1.phone=phone
    f1.image=img
    f1.save()

    print(request.POST['fname'])

    return redirect("firsttemplate")
  else :
    return render(request,"addstudent.html")
#add student function end..

#edit student function start...
def edit_student(request,id):
  if request.method =="POST":

    fname = request.POST['fname']
    lname = request.POST['lname']  
    age = request.POST['age']
    email = request.POST['email']
    phone = request.POST['phone']
    img = request.FILES['img']

    f1 = student.objects.get(id=id)
    f1.firstname=fname
    f1.lastname=lname
    f1.age=age
    f1.email=email
    f1.phone=phone
    f1.image=img
    f1.save()

    print(request.POST['fname'])

    return redirect("firsttemplate")
  else :
    e1 = student.objects.get(id=id)
    context ={
    'e1' : e1
    }
    
    return render(request,"editstudent.html",context)
#edit student function end..

#delete student function start
def delete_student(request,id):
  e1 = student.objects.get(id=id)
  e1.delete()
  return redirect("firsttemplate")
#delete student function end

#functions of subject table

def sub(request):
  s1 = subject.objects.all()
  
  context ={
    's1' : s1
  }
  print(s1)
  for i in s1:
    print(i.student_id.firstname)

  return render(request,"showsubject.html",context)

#add subject function start...
def add_subject(request):
  if request.method =="POST":
    print("inside add_subject")
    studentid = request.POST['stu_id']
    subjectnm = request.POST['sub_name']  
    chap = request.POST['cha']
    desc = request.POST['des']
    
    f = student.objects.get(id=studentid)
    f1 = subject()
    f1.student_id=f
    f1.subjectname=subjectnm
    f1.chapter=chap
    f1.description=desc
    f1.save()

    return redirect("showsubject")
  else :
    e = student.objects.all()
    context = {'e':e}
    return render(request,"addsubject.html",context)
#add subject function end..

#edit subject function start...
def edit_subject(request,id):
  

  if request.method =="POST":
    
    studentid = request.POST['stu_id']
    subjectnm = request.POST['sub_name']  
    chap = request.POST['cha']
    desc = request.POST['des']

    stu_obj=student.objects.get(id=studentid)
    f1 = subject.objects.get(id=id)
    f1.student_id=stu_obj
    f1.subjectname=subjectnm
    f1.chapter=chap
    f1.description=desc
    f1.save()

    print(request.POST['sub_name'])

    return redirect("showsubject")
  else :
    e1 = subject.objects.get(id=id)
    e = student.objects.all()
    context ={
    'e1' : e1,
    'e' : e
    }
    
    return render(request,"editsubject.html",context)
#edit subject function end..

#delete student function start
def delete_subject(request,id):
  e1 = subject.objects.get(id=id)
  e1.delete()
  return redirect("showsubject")
#delete student function end