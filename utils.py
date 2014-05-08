import datetime
from django.forms.models import model_to_dict

from core.models import *

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def  validate_data(title, content, tags, category_selected):
    errors = {}
    if category_selected == "Choose Category":
        errors['category_error'] = True
    if title == "" or len(title) < 5:
        errors['title_error'] = True
    if content == "" or len(content) < 20:
        errors['content_error'] = True
    if tags == "" or len (tags) < 5:
        errors['tags_error'] = True
    return errors

def save_text(title,text,tags,category):
    time = str(datetime.datetime.now())
    TextTable.objects.create(title=title,text=text,tags=tags,timestamp=time,category=category)

def save_feedback(comment, ip_address):
    time = str(datetime.datetime.now())
    VisitorFeedback.objects.create(ip = ip_address, comments = comment,timestamp = time)

def retrieve_data():
    return TextTable.objects.all().order_by('-timestamp')

def search_tag(tag):
    return TextTable.objects.filter(tags=tag).order_by('-timestamp')

def get_category():
    return Category.objects.all().order_by('name')

def save_media(title,text,tags,url):
    time =  str(datetime.datetime.now())
    TextTable.objects.create(title=title,text=text,tags=tags,url=url,timestamp=time)
