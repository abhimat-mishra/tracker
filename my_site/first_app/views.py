from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseNotFound,Http404

# Create your views here.

articles = {
    'sports' : 'Sports Page',
    'finance' : 'Finance Page',
    'politics' : 'Politics Page'
}

def news_view(request,topic):
    try:
        result=articles[topic]
        return HttpResponse(articles[topic])
    except:
        raise Http404("404 GENERIC ERROR")
        # result = f'Can not find page for this {topic} topic!'
        # return HttpResponseNotFound(result)

def add_view(request,num1,num2):
    add_result =num1+num2
    result = f"{num1}+{num2} = {add_result}"
    return HttpResponse(str(result))

# def sports_view(request):
#     return HttpResponse(articles['sports'])
# def finance_view(request):
#     return HttpResponse(articles['finance'])
# def politics_view(request):
#     return HttpResponse(articles['politics'])