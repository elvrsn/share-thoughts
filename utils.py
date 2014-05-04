import datetime
from django.forms.models import model_to_dict

from core.models import *

def save_text(title,text,tags,category):
    time = str(datetime.datetime.now())
    TextTable.objects.create(title=title,text=text,tags=tags,timestamp=time,category=category)

def retrieve_data():
    return TextTable.objects.all().order_by('-timestamp')

def search_tag(tag):
    return TextTable.objects.filter(tags=tag).order_by('-timestamp')

def get_category():
    return Category.objects.all().order_by('name')

def save_media(title,text,tags,url):
    time =  str(datetime.datetime.now())
    TextTable.objects.create(title=title,text=text,tags=tags,url=url,timestamp=time)
