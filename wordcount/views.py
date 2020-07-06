from django.http import HttpResponse
from django.shortcuts import render

def  home(request):
    return render(request,'home.html',{'hello':'there'})
def fun1(request):
    return HttpResponse('Welcome to my homepage')
def count(request):
    an1=request.GET['inp1']
    an2=request.GET['inp2']
    ans1=an1+an2
    return render(request,'count.html',{'ans':ans1},{'ana':an1})
