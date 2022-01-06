from django.shortcuts import render, redirect
from .models import *
import requests
# Create your views here.




def index(request):
    company = Company.objects.last()
    brand = Brand.objects.all().order_by('-id')[:6]
    banner = Banner.objects.last()
    content21_text = CONTENT21_text.objects.last()
    content21_obj = CONTENT21_obj.objects.all().order_by('-id')[:3]
    content21_obj2 = CONTENT21_obj2.objects.all().order_by('-id')[:3]
    call06 = CALL06.objects.last()
    features06_text = FEATURES06_text.objects.last()
    features06_obj = FEATURES06_obj.objects.all().order_by('-id')[:6]
    video_title = Video_introduction_title.objects.last()
    video = Introduction_video.objects.all().order_by('-id')[:3]
    content22_section1 = CONTENT22_SECTION1.objects.last()
    content22_section1_obj = CONTENT22_SECTION1_obj.objects.all().order_by('-id')[:5]
    content22_section2 = CONTENT22_SECTION2.objects.last()
    content22_section2_obj = CONTENT22_SECTION2_obj.objects.all().order_by('-id')[:2]
    content22_section3 = CONTENT22_SECTION3.objects.last()
    content22_section3_obj = CONTENT22_SECTION3_obj.objects.all().order_by('-id')[:6]
    content23 = CONTENT23.objects.last()
    portfolio07 = PORTFOLIO07.objects.last()
    portfolio07_image = PORTFOLIO07_image.objects.all()[:8]
    portfolio07_obj = PORTFOLIO07_obj.objects.all().order_by('-id')[:3]
    testimonals = TESTIMONALS.objects.last()
    testimonals_text = TESTIMONALS_text.objects.all().order_by('-id')[:3]
    form_text = DOWNLOAD01_form_text.objects.last()
    
    context = {
        'company': company,
        'brand': brand,
        'banner': banner,
        'content21_text': content21_text,
        'content21_obj': content21_obj,
        'content21_obj2': content21_obj2,
        'call06': call06,
        'features06_text': features06_text,
        'features06_obj': features06_obj,
        'video_title': video_title,
        'video': video,
        'content22_section1': content22_section1,
        'content22_section1_obj': content22_section1_obj,
        'content22_section2': content22_section2,
        'content22_section2_obj': content22_section2_obj,
        'content22_section3': content22_section3,
        'content22_section3_obj': content22_section3_obj,
        'content23': content23,
        'portfolio07': portfolio07,
        'portfolio07_image': portfolio07_image,
        'portfolio07_obj': portfolio07_obj,
        'testimonals': testimonals,
        'testimonals_text': testimonals_text,
        'form_text': form_text,
        
    }
    return render(request, 'index.html', context)


def get_number(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        contact = Clients.objects.create(name=name, phone_number=phone_number)
        contact.save()
        text = "Xabar\nIsmi : "+name+"\nTelefon raqami : "+phone_number
        url = "https://api.telegram.org/bot5029250236:AAH4w9lFmvF8UfLX_IWUB9-2ubcexgx4THE/sendMessage?chat_id="
        chat_id = Chat_id.objects.all()
        for id in chat_id:
            requests.get(url+str(id.chat_id)+'&text='+text)

    return redirect('index')
        
