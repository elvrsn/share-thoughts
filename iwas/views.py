from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from recaptcha.client import captcha

from utils import *

#def get_client_ip(request):
#    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#    if x_forwarded_for:
#        ip = x_forwarded_for.split(',')[0]
#    else:
#        ip = request.META.get('REMOTE_ADDR')
#    return ip

def home(request):
    contents = retrieve_data()
    for content in contents:
        content.tags = content.tags.split(',')
    return render_to_response('home.html',{'share':True,'contents':contents},context_instance=RequestContext(request))

def toshare(request):
    remote_address =  get_client_ip(request)
    context_dict = {}
    if request.method=='POST':
        title = request.POST.get('title','')
        content = request.POST.get('content','')
        tags = request.POST.get('tags','')
        category_selected = request.POST.get('category_selected','')
        response = captcha.submit(request.POST.get('recaptcha_challenge_field',''),
                                  request.POST.get('recaptcha_response_field',''),
                                  '6LctCPMSAAAAAEW17EABD3SDTgvCclUnT058mwxN',
                                  remote_address)
        context_dict['errors'] = validate_data(title, content, tags, category_selected)
        if not response.is_valid:
            context_dict['captcha_error'] = True
        else:
            save_text(title,content,tags,category)
            return HttpResponseRedirect(reverse("thanks_page"))
    context_dict['options'] = get_category()
    context_dict.update(csrf(request))
    return render_to_response('share.html',context_dict,context_instance=RequestContext(request))

def thanks(request):
    return render_to_response('thanks.html',{'share':True},context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html',{'share':True},context_instance=RequestContext(request))

def feedback(request):
    return render_to_response('feedback.html',{'share':True},context_instance=RequestContext(request))

def feedback_thanks(request):
    if request.method=='POST':
        ip_address = get_client_ip(request)
        comment = request.POST.get('feedback','')
        save_feedback(comment, ip_address)
    return render_to_response('feedback_thanks.html',{'share':True},context_instance=RequestContext(request))
