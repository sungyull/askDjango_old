from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView
import os
from django.conf import settings


class PostListView1(View):
    def get(self, request):
        name = 'LEESUNGYULL'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return """
            <h1>Ask Django </h1>
            <p>{name}</p>
            <p>파이선 장고 중..... </p>  
        """

post_list1 = PostListView1.as_view()

class PostListView2(TemplateView):
    template_name = """dojo/post_list.html"""

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = 'lee sung yull'
        return context

post_list2 = PostListView2.as_view()

class PostListView3(View):

    def get(self,request):
        return JsonResponse(self.get_data(),json_dumps_params={'ensure_ascii':False})

    def get_data(self):
        return {
        'message':'안녕 파이썬 장고',
        'items':['Python','장고','믄','AWS'],
        }

post_list3 = PostListView3.as_view()


class excel_down(View):
    def get(self, request):
        filepath = os.path.join(settings.BASE_DIR, 'tests.xls')
        filename = os.path.basename(filepath)
        with open(filepath, 'rb') as f:
            response = HttpResponse(f, content_type='application/vnd.ms-excel')
            # 필요한 응답헤더 세팅
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
            return response


post_list4 = excel_down.as_view()




