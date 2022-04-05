from math import fabs
from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from user.models import User
from shop.models import Config
from django.contrib.auth.hashers import make_password, check_password
from django.http import Http404
from cs.models import Board
from django.core.paginator import Paginator  
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

        if not(email and password):
            context['error'] = '모든 값을 입력해야 합니다.'
        else:

            try:
                user = User.objects.get(email = email)
            except:
                return HttpResponse(f'''
                    <script>
                        alert("존재하지 않는 아이디입니다!");
                        history.back();
                    </script>
                ''')

            if user.admin:
                if user.password == password:
                    request.session['user'] = user.id
                    request.session['admin'] = user.admin
                    return redirect('/whitevalley/')
                else:
                    context['error'] = '비밀번호가 틀렸습니다.'
            else:
                if check_password(password, user.password):
                    request.session['user'] = user.id
                    request.session['admin'] = user.admin
                    return redirect('/whitevalley/')
                else:
                    context['error'] = '비밀번호가 틀렸습니다'                   
        
    return render(request, 'login.html', context)


def logout(request):
    del(request.session["user"])
    del(request.session["admin"])

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

        if not(email and password and re_password and contact):
            context['error'] = '모든 값을 입력해야 합니다'
        elif password != re_password:
            context['error'] = '비밀번호가 다릅니다.'
        elif (User.objects.filter(email=email).exists()) == True :
            context['error'] = '사용중인 이메일입니다.'
        else:
            cnt = 0
            el = email.split("@")[0] # 이메일에서 @ 전까지를 닉네임이므로 값가져와서 split

            while 1:
                try:
                    User.objects.get(nickname=el)
                    el = email.split("@")[0] + "@" + str(cnt + 1)
                except:
                    break

            user = User(
                email = email,
                password = make_password(password),
                contact = contact,
                nickname = el
            )                
            user.save()
            return HttpResponse(f'''
                <script>
                    alert("회원가입에 성공했습니다!")
                    location.href = '/whitevalley/user/login/'
                </script>
            ''')

        return render(request, 'register.html', context)
    

def find_pw(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'login'
    }

    if request.method == 'GET':
        return render(request, 'find_pw.html', context)
    elif request.method == 'POST':
        email = request.POST.get('useremail')

        if not email:
            context['error'] = '이메일 입력바랍니다.'
        elif not User.objects.filter(email = email):
            context['error'] = '이메일이 없습니다.'
        elif User.objects.filter(email = email):

            return redirect(f'/whitevalley/user/chpw/${email}')  # 이메일 값을 url로 저장하고 보낸다.

        return render(request, 'find_pw.html', context)


def chpw(request, email):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'login'
    }

    if request.method == "GET":
        return render(request, "chpw.html",context)

    elif request.method == "POST":
        new_password = request.POST.get('new_password')
        re_password = request.POST.get('re_password')

        if not(new_password and re_password):
            context['error'] = '빈칸 없이 입력해주시길 바랍니다.'

        elif new_password != re_password:
            context['error'] = '비밀번호가 다릅니다.'

        elif new_password == re_password:
            
            user = User.objects.get(email = email.replace("$",""))
            user.password = make_password(new_password)
            user.save()

            return render(request, 'chpwOk.html', context)

        return render(request, "chpw.html",context)

def magazine_list(request):

    allmagazine = Board.objects.filter(tag='매거진').order_by('-reg_date')
    page = request.GET.get('page', '1')
    paginator = Paginator(allmagazine, 10)
    page_obj = paginator.get_page(page)

    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'magazine',
        'boards': page_obj,
        'magazine' : page_obj,
    }

    return render(request, 'm_list.html', context)


def magazine_detail(request, pk):
    board = Board.objects.get(pk=pk)
    board.view_cnt += 1
    board.save()

    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'magazine',
        'board' : board,
    }

    return render(request, 'm_detail.html', context)

def magazine_update(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'magazine',
    }

    return render(request, 'm_update.html')

# def magazine_update(request, pk):

#     context = {
#         'session': request.session,
#         'config': Config.objects.get(id=1),
#         'currentpage': 'magazine',
#         'board' : board,
#     }

#     if request.method == "GET":
#         try:
#             board = Board.objects.get(pk=pk)
#         except Board.DoesNotExist:
#             raise Http404('게시글을 찾을수 없습니다')

#         return render(request, 'm_update.html', context)
    
#     elif request.method == "POST":
#         title = request.POST['title']
#         content = request.POST['content']

#         # 수정
#         board = Board.objects.get(pk=pk)
#         board.title = title
#         board.content = content
#         board.save()   # UPDATE

#         return render(request, 'm_updateOk.html', {"pk": board.pk })
#     return render(request, 'm_update.html', pk)

def magazine_write(request):

    context = {
            'session': request.session,
            'config': Config.objects.get(id=1),
            'currentpage': 'magazine'
    }
    if request.method == 'GET':
        return render(request, 'm_write.html', context)

    elif request.method == 'POST':
        user = User.objects.get(id=request.session['admin'])
        tag = request.POST['magazine']
        title = request.POST['title']
        content = request.POST['content']


        b = Board(user = user, tag = tag, title = title, content = content)
        b.save()
        return render(request, 'm_writeOk.html', {"pk": b.pk})

def magazine_delete(request):

    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'magazine'
    }
    if request.method == "POST":
        id = request.POST['id']
        board = Board.objects.get(id=id)
        board.delete()

    return render(request, 'm_deleteok.html', context)


# ------------------------------------------------------------------------------------

def mypage(req):
    context = {
        'session': req.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'mypage'
    }

    context['user'] = User.objects.get(id=req.session['user'])

    return render(req, 'mypage.html', context)

def info_modify(req):
    password = req.GET["password"]
    real_password = req.GET["real_password"]

    if check_password(password, real_password):
        req.session['modify_check'] = True
        return HttpResponse(f'''
            <script>
                alert("인증이 완료되었습니다!!");
                location.href="/whitevalley/user/mypage/modify/detail/"
            </script>
        ''')
    else:
        return HttpResponse(f'''
            <script>
                alert("비밀번호가 틀렸습니다!!");
                history.back();
            </script>
        ''')


def info_modify_detail(req):
    try:
        req.session['user']
    except:
        return HttpResponse(f'''
            <script>
                alert("올바른 경로가 아닙니다.");
                history.back();
            </script>
        ''')

    try:
        req.session['modify_check']
    except:
        return HttpResponse(f'''
            <script>
                alert("인증 유효기간이 지났습니다. 다시 인증해주세요.");
                history.back();
            </script>
        ''')
    

    return render(req, 'mypage_modify.html')


def api_login(req):
    email = req.POST['api_email']
    password = req.POST['api_password']

    try:
        req.session['user'] = User.objects.get(email=email).id
        req.session['admin'] = User.objects.get(email=email).admin

        return HttpResponse(f'''
            <script>
                alert("로그인에 성공하였습니다!");
                location.href = '/whitevalley/';
            </script>
        ''')
    except:
        cnt = 0
        nickname = req.POST['api_nickname']

        while 1:
            try:
                User.objects.get(nickname=nickname)
                nickname = req.POST['api_nickname'] + "@" + str(cnt + 1)
            except:
                break

        user = User(email=email, nickname=nickname, password=password, contact='010-0000-0000')

        user.save()

        req.session['user'] = user.id
        req.session['admin'] = user.admin

        return HttpResponse(f'''
            <script>
                alert("카카오 계정으로 가입 완료되었습니다!!");
                location.href = '/whitevalley/';
            </script>
        ''')