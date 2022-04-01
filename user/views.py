from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from .models import User

#비밀번호 변경
from django.contrib.auth.hashers import check_password
from django.contrib import messages, auth

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            request.session['username'] = User.objects.get(email=username, password=password).email
            return HttpResponse(f'''
                <script>
                    alert("로그인에 성공했습니다!")
                    location.href = '/whitevalley/'
                </script>
            ''')
        except:
            return HttpResponse(f'''
                <script>
                    alert("존재하지 않는 아이디이거나 비밀번호가 일치하지 않습니다!");
                    history.back();    
                </script>
            ''')

def logout(request):
    del(request.session["username"])

    return redirect('/whitevalley/')

@csrf_exempt
def register(request):
# GET방식. 회원 가입 폼

    if request.method == 'GET':

        return render(request, 'register.html')

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
            user = User(
                email = email,
                password = make_password(password),
                contact = contact,
                nickname = email
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

