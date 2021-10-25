import random


from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Questions,User
import random

# Create your views here.
def login(request):
    if "user" in request.session:
        return redirect("question")

    return render(request,"login.html",{})

def logout(request):
    del request.session['user']
    return render(request, "login.html", {})


def checkuser(request):
    uname = request.POST['username']
    password = request.POST['password']
    print(uname)
    print(password)
    x = User.objects.filter(username=uname).filter(password=password).count()
    print(x)
    if x>=1:
        request.session['user'] = uname
        return redirect("question")
    else:
        return redirect("login")

def registration(request):
    return render(request, "register.html", {})



def register(request):
    username = request.POST['username']
    email = request.POST['email']
    mobile = request.POST['mobile']
    pw = request.POST['password']
    data = User.objects.all()
    print(data)
    print(mobile)
    obj=User(username=username,email=email,password=pw,mobilenumber=mobile)
    obj.save()

    return render(request,"login.html",{"data":data})
def question(request):
    name = request.session['user']
    all_question=Questions.objects.all()
    questions=[]

    for i in all_question:
        questions.append(i)
    random.shuffle(questions)
    result=[]
    index=0
    for i in questions:
        index+=1
        result.append([index,i.question,i.optiona,i.optionb,i.optionc])
    return render(request,"question.html",{"q":result,"j":1,"username":name})
def calculatemark(request):
    answer=""
    mark=0
    question_count=Questions.objects.all().count()
    for i in range(1,question_count+1):
        qname=request.POST[str(i)]
        answer+=request.POST[qname]
        mark+=Questions.objects.filter(question=qname).filter(answer=request.POST[qname]).count()
    return HttpResponse(f"<h1>Total Mark={mark}</h1>")


