import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def mysum(request, numbers):
    # numbers = "1/12121/1212/1/21/21/21/2/12/1/2"
    rtn = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(rtn)


def myname(request, name="""QQQ""", age=10):
    return HttpResponse( """{}, 안녕하세요. {}살 이네요?""".format(name, age))


def post_list1(request):
    name = '공유1'
    return HttpResponse("""
    <h1>Ask Django </h1>
    <p>{name}</p>
    <p>파이선 장고 중..... </p>    
    """.format(name = name))


def post_list2(request):
    name = '공유2'
    return render(request, 'dojo/post_list.html', {'name':name})


def post_list3(request):
    return JsonResponse({
        'message':'안녕 파이썬 장고',
        'items':['Python','장고','믄','AWS'],
    }, json_dumps_params={'ensure_ascii':False})


def excel_down(request):
    #filepath = """D:/DJHome/askDjango/dojo/tests.xls"""
    filepath = os.path.join(settings.BASE_DIR, 'tests.xls')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        # 필요한 응답헤더 세팅
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response