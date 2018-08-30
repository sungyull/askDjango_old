from django.http import HttpResponse
from django.shortcuts import render

def mysum(request, numbers):
    # numbers = "1/12121/1212/1/21/21/21/2/12/1/2"
    rtn = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(rtn)

def myname(request, name="""QQQ""", age=10):
    return HttpResponse( """{}, 안녕하세요. {}살 이네요?""".format(name, age))
