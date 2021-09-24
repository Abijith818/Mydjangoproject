from django.shortcuts import render
from django.http import HttpResponse

def testfun(request):
    return HttpResponse ('hello brothers')

def testfun1(request):
    return render(request,'new.html') 
