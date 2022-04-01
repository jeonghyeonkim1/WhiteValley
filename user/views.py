import email
from django.shortcuts import render, HttpResponse, redirect
from user.models import User
from shop.models import Config
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def login(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'login'
    }

    if request.method == "GET":
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        res_data = {}

        if not(email and password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        else:

            user = User.objects.get(email = email)

            if user.admin:
                if user.password == password:
                    request.session['user'] = user.id
                    request.session['admin'] = user.admin
                    return redirect('/whitevalley/')
                else:
                    res_data['error'] = '비밀번호가 틀렸습니다.'
            else:
                if check_password(password, user.password):
                    request.session['user'] = user.id
                    request.session['admin'] = user.admin
                    return redirect('/whitevalley/')
                else:
                    res_data['error'] = '비밀번호가 틀렸습니다'
        
    return render(request, 'login.html', res_data)

def logout(request):
    del(request.session["user"])

    return redirect('/whitevalley/')

def register(request):
# GET방식. 회원 가입 폼
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'sign'
    }

    if request.method == 'GET':

        return render(request, 'register.html', context)

    # POST방식. 회원 가입 처리
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re-password']
        contact = request.POST['contact']

        res_data = {}

        if not(email and password and re_password and contact):
            res_data['error'] = '모든 값을 입력해야 합니다'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.' # 작동안됨.
        else:
            el = email.split("@") # 이메일에서 @ 전까지를 닉네임이므로 값가져와서 split
            user = User(
                email = email,
                password = make_password(password),
                contact = contact,
                nickname = el[0]
            )
                
            user.save()
            return HttpResponse(f'''
                <script>
                    alert("회원가입에 성공했습니다!")
                    location.href = '/whitevalley/'
                </script>
            ''')

        return render(request, 'register.html', res_data)
    

def find_pw(request):
    return render(request,'find_pw.html')

def magazine_list(request):
    return render(request, 'm_list.html')

# 이거 ui설계용이므로 삭제 필수
def magazine_detail(request):
    return render(request, 'm_detail.html')

# def magazine_detail(request, pk):
#     return render(request, 'm_detail.html', pk)


# 이거 ui설계용이므로 삭제 필수
def magazine_update(request):
    return render(request, 'm_update.html')

# def magazine_update(request, pk):
#     return render(request, 'm_update.html', pk)

def magazine_write(request):
    return render(request, 'm_write.html')

def magazine_delete(request):
    return render(request, 'm_deleteok.html')

def mypage(req):
    context = {
        'session': req.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'mypage'
    }

    context['user'] = User.objects.get(id=req.session['user'])

    return render(req, 'mypage.html', context)