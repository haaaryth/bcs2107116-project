from django.shortcuts import render
from .models import student

# Create your views here.

def index(request):
    if request.method == 'GET':
        data = student.objects.filter(id=request.GET.get('s_id'))
        if len(data)==1:
            for value in data:
                if value.password=='NULL' and request.GET.get('s_pass')== 'NULL' :
                    dict={
                            'message':"Please sign in first"
                        }
                    return render (request,'index.html',dict) 

                elif value.password==request.GET.get('s_pass') :
                    return render (request,'search_student.html')
                else:
                    dict={
                        'message':"invalid password"
                    }
                    return render (request,'index.html',dict)
                       
        else:
            dict={
                        'message':" "
                    }
            return render (request,'index.html', dict)

def search_student(request):
    return render (request,'search_student.html')

def welcome(request):
    return render (request,'welcome.html')

def signup(request):
    return render (request,'signup.html')