from django.shortcuts import render,redirect

# Create your views here.
def order(request):
    return render(request,'order.html')

def order_des(request):
   
    return render(request, 'order_des.html')

def custom1(request):
   
    return render(request, 'custom1.html')

    
def custom2(request):
   
    return render(request, 'custom2.html')

def customend(request):
   
    return render(request, 'customend.html')

def payment(request):
    return render(request,'payment.html')

def loading(request):
    return render(request, 'loading.html')
    
#    if request.method == "POST":
#         URL = 'https://kapi.kakao.com/v1/payment/ready'
#         headers = {
#             "Authorization": "KakaoAK " + "953b61f21c9f3ddc6d49f10981368940",   # 변경불가
#             "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
#         }
#         params = {
#             "cid": "TC0ONETIME",    # 테스트용 코드
#             "partner_order_id": "1001",     # 주문번호
#             "partner_user_id": "german",    # 유저 아이디
#             "item_name": "연어초밥",        # 구매 물품 이름
#             "quantity": "1",                # 구매 물품 수량
#             "total_amount": "12000",        # 구매 물품 가격
#             "tax_free_amount": "0",         # 구매 물품 비과세
#             "approval_url": "paySuccess/",
#             "cancel_url": "payCancel/",
#             "fail_url": "payFail/",
#         }

#         res = requests.post(URL, headers=headers, params=params)
#         request.session['tid'] = res.json()['tid']      # 결제 승인시 사용할 tid를 세션에 저장
#         next_url = res.json()['next_redirect_pc_url']   # 결제 페이지로 넘어갈 url을 저장
#         return redirect(next_url)
    
   

def payFail(request):
    return render(request, 'payFail.html')
def payCancel(request):
    return render(request, 'payCancel.html')