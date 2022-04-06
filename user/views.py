from django.shortcuts import render, HttpResponse, redirect
from user.models import User
from shop.models import Config
from django.contrib.auth.hashers import make_password, check_password
from django.http import Http404
from cs.models import Board, B_Photo, Photo_Upload
from django.core.paginator import Paginator  
import re

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
        email = request.POST['useremail']

        if not email:
            context['error'] = '이메일 입력바랍니다.'
        elif not User.objects.filter(email = email):
            context['error'] = '이메일이 없습니다.'
        elif User.objects.filter(email = email):

            return redirect(f'/whitevalley/user/chpw/${email}/')
                            
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
    photos = B_Photo.objects.all()

    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'magazine',
        'boards': page_obj,
        'photos' : photos,
    }

    return render(request, 'm_list.html', context)


def magazine_detail(request, pk):

    magazine = Board.objects.get(pk=pk)
    photos = B_Photo.objects.get(board = pk)
    magazine.view_cnt += 1
    magazine.save()

    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'magazine',
        'magazine' : magazine,
        'photos' : photos,
    }
    # print('포토는 ', photos)
    return render(request, 'm_detail.html', context)

def magazine_update(request, pk):

    if request.method == "GET":
        magazine = Board.objects.get(pk=pk)
        context = {
            'session': request.session,
            'config': Config.objects.get(id=1),
            'currentpage': 'magazine',
            'magazine' : magazine,
        }

        return render(request, 'm_update.html', context)
    
    elif request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']

        magazine = Board.objects.get(pk=pk)
        magazine.title = title
        magazine.content = content
        magazine.save()

        return render(request, 'm_updateOk.html', {"pk": magazine.pk})

def magazine_write(request):
  
    context = {
            'session': request.session,
            'config': Config.objects.get(id=1),
            'currentpage': 'magazine',            
    }
    if request.method == 'GET':
        return render(request, 'm_write.html', context)
  
    elif request.method == 'POST':
        user = User.objects.get(id=request.session['admin'])
        tag = request.POST['magazine']
        title = request.POST['title']
        content = request.POST['content']
        uploadedFile = request.FILES["uploadedFile"]

        if len(re.findall(r'\W | [^.]', uploadedFile.name)) > 0:
            return HttpResponse(f'''
                <script>
                    alert("파일 이름에 특수문자가 포함되어 있습니다!");
                    history.back();
                </script>
            ''')

        uploadedFileName = re.sub(r"\W | [^.] | [^_]", "", uploadedFile.name.replace(" ", "_").replace("(", "").replace(")", ""))

        Photo_Upload(title=uploadedFileName, photo=uploadedFile).save()

        board = Board(
            user=user,
            tag=tag,
            title=title, 
            content=content, 
        )
        board.save()

        B_Photo(board=board, photo=f'/static/image/{uploadedFileName}').save()

        return render(request, 'm_writeOk.html', {"pk": board.pk})
  
def magazine_delete(request):

    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'magazine'
    }
    if request.method == "POST":
        id = request.POST['id']
        magazine = Board.objects.get(id=id)
        magazine.delete()

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
        res = render(req, HttpResponse(f'''
            <script>
                alert("인증이 완료되었습니다!!");
                location.href="/whitevalley/user/mypage/modify/detail/"
            </script>
        '''))

        res.set_cookie(
            key = 'modify_check',
            value = True,
        )
        
        return 
    else:
        return HttpResponse(f'''
            <script>
                alert("비밀번호가 틀렸습니다!!");
                history.back();
            </script>
        ''')


def info_modify_detail(req):
    context = {
        'session': req.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'mypage'
    }
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
        req.COOKIES['modify_check']
    except:
        return HttpResponse(f'''
            <script>
                alert("인증 유효기간이 지났습니다. 다시 인증해주세요.");
                history.back();
            </script>
        ''')

    render(req, 'mypage_modify.html', context)
    

    


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