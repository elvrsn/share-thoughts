from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf

from utils import *

def home(request):
    contents = retrieve_data()
    for content in contents:
        content.tags = content.tags.split(',')
    return render_to_response('home.html',{'share':True,'contents':contents},context_instance=RequestContext(request))

def toshare(request):
    context_dict = {}
    context_dict['options'] = get_category()
    context_dict.update(csrf(request))
    return render_to_response('share.html',context_dict,context_instance=RequestContext(request))

def thanks(request):
    if request.method=='POST':
        title = request.POST.get('title','')
        content = request.POST.get('content','')
        tags = request.POST.get('tags','')
        category = request.POST.get('category','')
        save_text(title,content,tags,category)
    return render_to_response('thanks.html',{'share':True},context_instance=RequestContext(request))

def shared(request):
    return HttpResponse("to do")

