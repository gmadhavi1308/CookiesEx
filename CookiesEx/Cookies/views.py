from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def create_cookie(request):
    response=HttpResponse("Cookie Created Successfully")
    response.set_cookie('user_name','Jackson')
    return response

def retrieve_cookie(request):
    try:
        if 'user_name' in request.COOKIES:
            user=request.COOKIES['user_name']
            return HttpResponse("Hello.."+user+" How are you ? Welcome to my DJango website.");
        else:
            return HttpResponse("Hello...guest,Welcome to my DJango website.")
    except Exception as ex:
        return HttpResponse(ex);

def count_visits(request):
    if 'count' in request.COOKIES:
        value=int(request.COOKIES['count'])+1
    else:
        value=1
    response=render(request,'count.html',{'count':value})
    response.set_cookie('count',value)
    return response
