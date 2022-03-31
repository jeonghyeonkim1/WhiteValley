from django.shortcuts import render, HttpResponse, redirect
from .models import User

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

def register(request):
    return render(request, 'register.html')

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

