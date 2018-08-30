from django.http import HttpResponse
from django.shortcuts import render

def mysum(request, x=0, y=0, z=0):
    #request :
    return HttpResponse(int(x) + int(y) + int(z))

def myname(request, name):
    return HttpResponse( name + """안녕하세요...!""")