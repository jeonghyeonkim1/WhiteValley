import base64
from random import random
from unittest import result
from django.shortcuts import render,redirect
from shop.models import Config
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse 
import os

# Create your views here.
def order(request):
    
    try:
        if request.session['user']:
            context = {
                'session': request.session,
                'config': Config.objects.get(id=1),
                'currentpage': 'shopping',
            }
            return render(request, 'order.html', context)
        elif request.session['admin']:
            context = {
                'session': request.session,
                'config': Config.objects.get(id=1),
                'currentpage': 'shopping',
            }
            return render(request, 'order.html', context)
        else:
            return HttpResponse(f'''
                <script>
                    alert("로그인이 필요한 페이지입니다.");
                    location.href='/whitevalley/shopping/loading2/';
                </script>
            ''')
        
    except:
        return HttpResponse(f'''
        
            <script>
                alert("로그인이 필요합니다.");
                location.href='/whitevalley/shopping/loading2/';
            </script>
        ''')
        
    
def order_des(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }
    return render(request, 'order_des.html',context)

def custom1(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }
    return render(request, 'custom1.html',context)

    
def custom2(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }
    return render(request, 'custom2.html',context)

def customend(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }
    return render(request, 'customend.html',context)

def payment(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }
    return render(request,'payment.html',context)

def loading(request):
    return render(request, 'loading.html')

def loading2(request):
    return render(request, 'loading2.html')

    
# @csrf_exempt
# def canvasToImage(request):
#     data = result.POST.__getitem__('data')
#     data = data[22:]
#     number = random.randrange(1,1000)

#     path = str(os.path.join(settings.STATIC_ROOT, 'static/image/'))
#     filename = 'image' + str(number) + '.png'

#     image = open(path+filename,"wb")
#     image.write(base64.b64decode(data))
#     image.close()

#     answer = {'filename':filename}
#     return JsonResponse(answer)


def payFail(request):
    return render(request, 'payFail.html')
def payCancel(request):
    return render(request, 'payCancel.html')