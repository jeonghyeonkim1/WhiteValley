from django.shortcuts import render, redirect
from shop.models import Config
from django.http import HttpResponse
import urllib.request
from user.models import User
from order.models import Cart, Order
from recommendation.models import Type, T_photo, Product, Tag_list
import os.path


# Create your views here.
def order(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        'types': Type.objects.all()
    }

    if (len(Type.objects.all()) != 0):
        pass
    else:
        Type(title="티셔츠", description="반팔입니다.", img="/static/image/products/shortw.png", price=19800).save()
        T_photo(title=Type.objects.get(title="티셔츠"), photo='/static/image/products/shortw.png', color="흰색").save()
        T_photo(title=Type.objects.get(title="티셔츠"), photo='/static/image/products/s_yellow.png', color="노란색").save()
        T_photo(title=Type.objects.get(title="티셔츠"), photo='/static/image/products/s_red.png', color="빨간색").save()
        T_photo(title=Type.objects.get(title="티셔츠"), photo='/static/image/products/s_purple.png', color="보라색").save()
        T_photo(title=Type.objects.get(title="티셔츠"), photo='/static/image/products/s_orange.png', color="오렌지색").save()
        T_photo(title=Type.objects.get(title="티셔츠"), photo='/static/image/products/s_navy.png', color="군청색").save()
        T_photo(title=Type.objects.get(title="티셔츠"), photo='/static/image/products/s_ivory.png', color="아이보리색").save()
        T_photo(title=Type.objects.get(title="티셔츠"), photo='/static/image/products/s_green.png', color="초록색").save()
        T_photo(title=Type.objects.get(title="티셔츠"), photo='/static/image/products/s_gray.png', color="회색").save()
        T_photo(title=Type.objects.get(title="티셔츠"), photo='/static/image/products/s_blue.png', color="파란색").save()
        T_photo(title=Type.objects.get(title="티셔츠"), photo='/static/image/products/s_black.png', color="검은색").save()
        T_photo(title=Type.objects.get(title="티셔츠"), photo='/static/image/products/s_babypink.png', color="핑크색").save()
        Type(title="긴팔", description="긴팔입니다.", img="/static/image/products/mtmw.png", price=25800).save()
        T_photo(title=Type.objects.get(title="긴팔"), photo='/static/image/products/mtmw.png', color="흰색").save()
        T_photo(title=Type.objects.get(title="긴팔"), photo='/static/image/products/m_yellow.png', color="노란색").save()
        T_photo(title=Type.objects.get(title="긴팔"), photo='/static/image/products/m_red.png', color="빨간색").save()
        T_photo(title=Type.objects.get(title="긴팔"), photo='/static/image/products/m_purple.png', color="보라색").save()
        T_photo(title=Type.objects.get(title="긴팔"), photo='/static/image/products/m_orange.png', color="오렌지색").save()
        T_photo(title=Type.objects.get(title="긴팔"), photo='/static/image/products/m_navy.png', color="군청색").save()
        T_photo(title=Type.objects.get(title="긴팔"), photo='/static/image/products/m_ivory.png', color="아이보리색").save()
        T_photo(title=Type.objects.get(title="긴팔"), photo='/static/image/products/m_green.png', color="초록색").save()
        T_photo(title=Type.objects.get(title="긴팔"), photo='/static/image/products/m_gray.png', color="회색").save()
        T_photo(title=Type.objects.get(title="긴팔"), photo='/static/image/products/m_blue.png', color="파란색").save()
        T_photo(title=Type.objects.get(title="긴팔"), photo='/static/image/products/m_black.png', color="검은색").save()
        T_photo(title=Type.objects.get(title="긴팔"), photo='/static/image/products/m_babypink.png', color="핑크색").save()
        Type(title="후드티", description="후드입니다.", img="/static/image/products/hoodw.png", price=31200).save()
        T_photo(title=Type.objects.get(title="후드티"), photo='/static/image/products/hoodw.png', color="흰색").save()
        T_photo(title=Type.objects.get(title="후드티"), photo='/static/image/products/h_yellow.png', color="노란색").save()
        T_photo(title=Type.objects.get(title="후드티"), photo='/static/image/products/h_red.png', color="빨간색").save()
        T_photo(title=Type.objects.get(title="후드티"), photo='/static/image/products/h_purple.png', color="보라색").save()
        T_photo(title=Type.objects.get(title="후드티"), photo='/static/image/products/h_orange.png', color="오렌지색").save()
        T_photo(title=Type.objects.get(title="후드티"), photo='/static/image/products/h_navy.png', color="군청색").save()
        T_photo(title=Type.objects.get(title="후드티"), photo='/static/image/products/h_ivory.png', color="아이보리색").save()
        T_photo(title=Type.objects.get(title="후드티"), photo='/static/image/products/h_green.png', color="초록색").save()
        T_photo(title=Type.objects.get(title="후드티"), photo='/static/image/products/h_gray.png', color="회색").save()
        T_photo(title=Type.objects.get(title="후드티"), photo='/static/image/products/h_blue.png', color="파란색").save()
        T_photo(title=Type.objects.get(title="후드티"), photo='/static/image/products/h_black.png', color="검은색").save()
        T_photo(title=Type.objects.get(title="후드티"), photo='/static/image/products/h_babypink.png', color="핑크색").save()
        redirect('/whitevalley/shopping/order/')

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
                'type_title': request.GET['type_title'],
                'type_price': request.GET['type_price'],
                'type_colors': T_photo.objects.filter(title=Type(title=request.GET['type_title'])),
                'type_current': Type.objects.get(title=Type(title=request.GET['type_title']))
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
                            break
                        

                    with open(f"static/image/uploaded_img/{name}", mode="wb") as f:
                        f.write(mem)
                        context['img_path'] = f'/static/image/uploaded_img/{name}'
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
    try:
        user = User.objects.get(id=request.session['user'])
    except:
        return HttpResponse(f'''
            <script>
                alert("로그인이 필요합니다.");
                location.href='/whitevalley/shopping/loading2/';
            </script>
        ''')

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
                r_location = request.POST['location_etc'] if request.POST['location'] == "기타사항" else request.POST['location'],
                r_pw = request.POST['r_pw_etc'] if request.POST['r_pw'] == "기타사항" else request.POST['r_pw']
            ).save()

            i.delete()
        
        
        user.point = user.point + (total_price // 10)

        try:
            user.point = user.point - int(request.POST['use_point'])
        except:
            pass

        user.save()

        return HttpResponse(f'''
            <script>
                alert("구매가 완료되었습니다!!");
                location.href = '/whitevalley/';
            </script>
        ''')

    return render(request, 'payment.html', context)
    

def loading(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
    }

    product = Product(
        user = User.objects.get(id=request.session['user']),
        type = Type.objects.get(title=request.POST['type_title']),
        size = request.POST['type_size'],
        request = request.POST['order_req'],
        img = request.POST['img_path']
    )

    product.save()

    # 태그 추가요망
    tag = Tag_list(name=request.POST['product_tag'])

    tag.save()

    tag.product.add(product)

    Cart(user=product.user, product=product, amount=request.POST['order_amount']).save()

    return render(request, 'loading.html',context)

def loading2(request):
    return render(request, 'loading2.html')


def payFail(request):
    return render(request, 'payFail.html')
def payCancel(request):
    return render(request, 'payCancel.html')