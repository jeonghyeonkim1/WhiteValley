from datetime import datetime
from django.shortcuts import render, redirect
from shop.models import Config
from django.http import HttpResponse
import urllib.request
from user.models import User
from order.models import Cart, Order
from recommendation.models import Type, Product
import os.path


# Create your views here.
def order(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        'types': Type.objects.all()
    }

    try:
        request.session['user']
        
        return render(request, 'order.html', context)

    except:
        return HttpResponse(f'''
            <script>
                alert("로그인이 필요합니다.");
                location.href='/whitevalley/shopping/loading2/';
            </script>
        ''')
        
    
def order_des(request):
    try:
        request.session['user']

        try:
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

        except:
            return HttpResponse(f'''
                <script>
                    alert("타입 설정이 완료되지 않았습니다!");
                    location.href='/whitevalley/shopping/order/';
                </script>
            ''')

    except:
        return HttpResponse(f'''
            <script>
                alert("로그인이 필요합니다.");
                location.href='/whitevalley/shopping/loading2/';
            </script>
        ''')

    

def custom1(request):
    try:
        request.session['user']
        try:
            context = {
                'session': request.session,
                'config': Config.objects.get(id=1),
                'currentpage': 'shopping',
                'type_price': request.GET['type_price'],
                'type_title': request.GET['type_title']
            }

            return render(request, 'custom1.html', context)

        except:
            return HttpResponse(f'''
                <script>
                    alert("타입 설정이 완료되지 않았습니다!");
                    location.href='/whitevalley/shopping/order/';
                </script>
            ''')

    except:
        return HttpResponse(f'''
            <script>
                alert("로그인이 필요합니다.");
                location.href='/whitevalley/shopping/loading2/';
            </script>
        ''')

    

def custom2(request):
    try:
        request.session['user']
        try:
            context = {
                'session': request.session,
                'config': Config.objects.get(id=1),
                'currentpage': 'shopping',
                'color': request.GET.get('color_input'),
                'type_size': request.GET.get('type_size'),
                'type_price': request.GET['type_price'],
                'type_title': request.GET['type_title']
            }

            return render(request, 'custom2.html', context)

        except:
            return HttpResponse(f'''
                <script>
                    alert("타입 설정이 완료되지 않았습니다!");
                    location.href='/whitevalley/shopping/order/';
                </script>
            ''')

    except:
        return HttpResponse(f'''
            <script>
                alert("로그인이 필요합니다.");
                location.href='/whitevalley/shopping/loading2/';
            </script>
        ''')



def customend(request):
    try:
        user = User.objects.get(id=request.session['user'])

        try:
            context = {
                'session': request.session,
                'config': Config.objects.get(id=1),
                'currentpage': 'shopping',
                'type_size':request.POST['type_size'],
                'type_price': request.POST['type_price'],
                'type_title': request.POST['type_title'],
                'user': user
            }

            if request.method == "POST":
                if request.POST['t_input'] == "0" and request.POST['s_input'] == "0" and request.POST['i_input'] == "0":
                    return HttpResponse(f'''
                        <script>
                            alert("적어도 하나 이상이 커스텀을 적용시켜 완성해주세요!");
                            history.back();
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

        except:
            return HttpResponse(f'''
                <script>
                    alert("타입 설정이 완료되지 않았습니다!");
                    location.href='/whitevalley/shopping/order/';
                </script>
            ''')

    except:
        return HttpResponse(f'''
            <script>
                alert("로그인이 필요합니다.");
                location.href='/whitevalley/shopping/loading2/';
            </script>
        ''')


def payment(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }

    user = User.objects.get(id=request.session['user'])
    context['user'] = user
    cart = Cart.objects.filter(user=user, checked="True")
    context['cart'] = cart

    context['adress'] = user.adress.split("_")

    total_price = 0
    for i in cart:
        total_price += i.product.type.price * i.amount

    if total_price == 0:
        return HttpResponse(f'''
            <script>
                alert("구매하실 수 있는 물품이 없습니다!");
                location.href = '/whitevalley/shopping/order/';
            </script>
        ''')
        
    else:
        context['total_price'] = total_price
        context['total_point'] = total_price // 10

    if request.method == 'POST':
        List = []
        for i in range(5):
            List.append(request.POST[f'adress{i}'])

        adress = "_".join(List)

        for i in cart:
            Order(
                user = User.objects.get(id=request.session['user']),
                product = i.product,
                amount = i.amount,
                state = "배송준비",
                delivery_req = request.POST['del_req'],
                r_name = request.POST['receiver'],
                r_adress = adress,
                r_contact = request.POST['contact'],
                r_location = request.POST['location']
            ).save()

            i.delete()

        try:
            user.point = user.point - int(request.POST['use_point']) + (total_price // 10)
            user.save()
        except:
            pass

        return HttpResponse(f'''
            <script>
                alert("구매가 완료되었습니다!!");
                location.href = '/whitevalley/';
            </script>
        ''')

    return render(request, 'payment.html', context)

    # except:
    #     return HttpResponse(f'''
    #         <script>
    #             alert("로그인이 필요합니다.");
    #             location.href='/whitevalley/shopping/loading2/';
    #         </script>
    #     ''')

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