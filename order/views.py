from django.shortcuts import render, redirect
from shop.models import Config
from django.http import HttpResponse
import urllib.request
from user.models import User
from order.models import Cart
from recommendation.models import Type, Product
import os.path


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
    size = request.GET.get('type_size')
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        'color': color,
        'type_size':size,
        'type_price': request.GET['type_price'],
        'type_title': request.GET['type_title']
    }

    return render(request, 'custom2.html',context)


def customend(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        'type_size':request.POST['type_size'],
        'type_price': request.POST['type_price'],
        'type_title': request.POST['type_title']
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

            mem = urllib.request.urlopen(url).read()
            cnt = 0
            name = f'img{cnt}.jpg'

            while os.path.exists(f'static/image/uploaded_img/{name}'):
                cnt += 1
                name = f'img{cnt}.jpg'

                if os.path.exists(f'static/image/uploaded_img/{name}') == False:
                    context['img_path'] = f'/static/image/uploaded_img/{name}'
                    break
                

            with open(f"static/image/uploaded_img/{name}", mode="wb") as f:
                f.write(mem)
                print("이미지 저장 완료되었습니다.")

            return render(request, 'customend.html', context)


def payment(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }
    context['user'] = User.objects.get(id=request.session['user'])

    return render(request,'payment.html',context)

def loading(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        'tag': request.POST['product_tag']
    }

    product = Product(
        user = User.objects.get(id=request.session['user']),
        type = Type.objects.get(title=request.POST['type_title']),
        size = request.POST['type_size'],
        request = request.POST['order_req'],
        img = request.POST['img_path']
    )

    product.save()

    Cart(user=product.user, product=product, amount=request.POST['order_amount']).save()

    return render(request, 'loading.html',context)

def loading2(request):
    return render(request, 'loading2.html')


def payFail(request):
    return render(request, 'payFail.html')
def payCancel(request):
    return render(request, 'payCancel.html')