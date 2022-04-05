from django.shortcuts import render, redirect
from shop.models import Config
from django.http import HttpResponse
import urllib.request
from user.models import User
from recommendation.models import Type


# Create your views here.
def order(request):
    try:
        context = {
            'session': request.session,
            'config': Config.objects.get(id=1),
            'currentpage': 'shopping',
            'types': Type.objects.all()
        }
        if request.session['user']:
            
            return render(request, 'order.html', context)
        elif request.session['admin']:

            context['title'] = request.title

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
        'currentpage': 'shopping',
        'type_price': request.GET['type_price'],
        'type_desc': request.GET['type_desc'],
        'type_img': request.GET['type_img'],
        'type_title': request.GET['type_title']
    }

    return render(request, 'order_des.html', context)

def custom1(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        'type_price': request.GET['type_price'],
        'type_title': request.GET['type_title']
    }

    return render(request, 'custom1.html',context)

def custom2(request):
    color = request.GET.get('color_input')
    size = request.GET.get('size_input')
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        'color': color,
        'size':size,
        'type_price': request.GET['type_price'],
        'type_title': request.GET['type_title']
    }

    return render(request, 'custom2.html',context)


def customend(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
    }
    context['user'] = User.objects.get(id=request.session['user'])
    

    if request.method == "POST":
        if request.POST['t_input'] == "0" and request.POST['s_input'] == "0" and request.POST['i_input'] == "0":
            return HttpResponse(f'''
                <script>
                    alert("적어도 하나 이상이 커스텀을 적용시켜 완성해주세요!");
                    window.history.back();
                </script>
            ''')
        else:
        
            url = request.POST['file_base']

            cnt = 0
        
            mem = urllib.request.urlopen(url).read()

            with open("static/image/uploaded_img/test3.jpg", mode="wb") as f:
                f.write(mem)
                print("이미지 저장 완료되었습니다.")
                
            return render(request, 'customend.html',context)


def payment(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }
    context['user'] = User.objects.get(id=request.session['user'])

    return render(request,'payment.html',context)

def loading(request):
    return render(request, 'loading.html')

def loading2(request):
    return render(request, 'loading2.html')


def payFail(request):
    return render(request, 'payFail.html')
def payCancel(request):
    return render(request, 'payCancel.html')