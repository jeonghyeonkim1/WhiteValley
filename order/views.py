from django.shortcuts import render, redirect
from shop.models import Config
from django.http import HttpResponse
import urllib.request
# import requests
from user.models import User


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

    # if request.POST['t_input'] == "0":
    #     return HttpResponse(f''' 
    #         <script>
    #             alert("커스텀을 하나 이상 적용시켜주세요!);
    #             window.history.back();
    #         </script>
    #     ''')

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
    # if request.method == "POST":
    #     URL = 'https://kapi.kakao.com/v1/payment/ready'
    #     headers = {
    #         'Authorization': "KaKaoAk" + "953b61f21c9f3ddc6d49f10981368940",
    #         'Content-type': "application/x-www-form-urlencoded;charset=utf-8",
    #     }
    #     params = {
    #         "cid": "TC0ONETIME",    # 테스트용 코드
    #         "partner_order_id": "1001",     # 주문번호
    #         "partner_user_id": "german",    # 유저 아이디
    #         "item_name": "연어초밥",        # 구매 물품 이름
    #         "quantity": "1",                # 구매 물품 수량
    #         "total_amount": "12000",        # 구매 물품 가격
    #         "tax_free_amount": "0",         # 구매 물품 비과세
    #         "approval_url": "결제 성공 시 이동할 url",
    #         "cancel_url": "결제 취소 시 이동할 url",
    #         "fail_url": "결제 실패 시 이동할 url",
    #     }
    #     res = requests.post(URL, headers=headers, params=params)
    #     request.session['tid'] = res.json()['tid']
    #     next_url = res.json()['next_redirect_pc_url']
    #     return redirect(next_url)

    return render(request,'payment.html',context)

def loading(request):
    return render(request, 'loading.html')

def loading2(request):
    return render(request, 'loading2.html')


def payFail(request):
    return render(request, 'payFail.html')
def payCancel(request):
    return render(request, 'payCancel.html')