from urllib import request
from django.shortcuts import render, HttpResponse, redirect
from user.models import User
from shop.models import Config
from django.contrib.auth.hashers import make_password, check_password
from django.http import Http404
from cs.models import Board, B_Photo, Photo_Upload
from django.core.paginator import Paginator  
import re
# from django.core.mail import send_mail #보내짐
from django.core.mail import EmailMultiAlternatives
# Create your views here.
def login(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'login'
    }

    if request.method == "GET":
        try:
            request.session['user']
            return HttpResponse(f'''
                <script>
                    alert("이미 로그인상태 입니다.");
                    location.href = '/whitevalley/';
            ''')
        except:
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
                    return HttpResponse(f'''
                        <script>
                            alert("로그인 성공하였습니다!");
                            location.href = '/whitevalley/';
                        </script>
                    ''')
                else:
                    context['error'] = '비밀번호가 틀렸습니다.'
                    
            else:
                if check_password(password, user.password):
                    request.session['user'] = user.id
                    request.session['admin'] = user.admin
                    return HttpResponse(f'''
                        <script>
                            alert("로그인 성공하였습니다!");
                            location.href = '/whitevalley/';
                        </script>
                    ''')
                else:
                    context['error'] = '비밀번호가 틀렸습니다'

    return HttpResponse(f'''
        <script>
            alert("로그인 실패하였습니다!");
            history.back();
        </script>
    ''') 

    
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
            # send_mail("안녕하세요. WhiteValley입니다.",
            # "안녕하세요. 회원가입을 축하드립니다. 정상적으로 이용이 가능합니다.",
            # "dbswlrl2@naver.com",
            # [user.email],
            # # html_message='hi.html',
            # fail_silently=False)

            subject, from_email, to = '안녕하세요. Plain Vally입니다.', 'dbswlrl2@naver.com', user.email
            text_content = 'This is an important message.'
            html_content = '<br><h1>회원가입 완료<h1><hr><br><strong>White Vally 회원가입을 축하드립니다.</strong><br>신규 회원 가입 해택으로 적립금 0000pt 지급되었습니다.<br>지금 바로, White Valley <a style="text-decoration:none;" href="http://127.0.0.1:8000/whitevalley/user/login/"> 로그인</a> 후 마이페이지에서 확인해보세요.<br><br><hr><h6>본 메일은 발신 전용 메일이며, 회신되지 않으므로 문의사항은 홈페이지 내 <a style="text-decoration:none;" href="http://127.0.0.1:8000/whitevalley/cs/faq/list/">고객센터</a>를 이용해주세요.<br>고객센터 TEL: 0000-0000<br>주식회사 Plain Valley | 서울특별시 강남구 신사동 640-2 로빈명품관  | 사업자등록번호 : 000-00-0000<br>| 대표 : OOO COPYRIGHTS (C)Plain Valley ALL RIGHTS RESERVED.<h6>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

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
    write_pages = int(request.session.get('write_pages', 5))
    per_page = request.session.get('per_page', 10)
    page = request.GET.get('page', 1)
    photos = B_Photo.objects.all()
    paginator = Paginator(allmagazine, per_page) 
    page_obj = paginator.get_page(page)

    start_page = ((int)((page_obj.number - 1) / write_pages) * write_pages) + 1
    end_page = start_page + write_pages - 1

    if end_page >= paginator.num_pages:
        end_page = paginator.num_pages


    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'magazine',
        'boards': page_obj,
        'photos' : photos,
        'write_pages': write_pages,
        'start_page': start_page,
        'end_page': end_page,
        'page_range': range(start_page, end_page + 1),
    }

    return render(request, 'm_list.html', context)

def magazine_detail(request, pk):

    magazine = Board.objects.get(pk=pk)
    photos = B_Photo.objects.get(board=pk)
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

    magazine = Board.objects.get(pk=pk)
    photos = B_Photo.objects.get(board=pk)

    if request.method == "GET":
        magazine = Board.objects.get(pk=pk)
        context = {
            'session': request.session,
            'config': Config.objects.get(id=1),
            'currentpage': 'magazine',
            'magazine' : magazine,
            'photos': photos,
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

    try:
        if request.method == 'GET':
            return render(request, 'm_write.html', context)
    
        elif request.method == 'POST':
            user = User.objects.get(id=request.session['user'])
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
    except:
        return HttpResponse(f'''
            <script>
                alert("사진 첨부해주세요!");
                history.back();
            </script>
        ''')

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
        res = HttpResponse(f'''
            <script>
                alert("인증이 완료되었습니다!!");
                location.href="/whitevalley/user/mypage/modify/detail/"
            </script>
        ''')

        res.set_cookie(
            key='modify_check',
            value=True,
            expires=300
        )
        
        return res
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
        user = User.objects.get(id=req.session['user'])
        context['user'] = User.objects.get(id=req.session['user'])
        context['adress'] = user.adress.split("_")

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
                location.href = '/whitevalley/user/mypage/';
            </script>
        ''')

    if req.method == "POST":
        try:
            if check_password(req.POST['pw2'], make_password(req.POST['pw1'])) == False:
                return HttpResponse(f'''
                    <script>
                        alert("비밀번호가 일치하지 않습니다!");
                        history.back();
                    </script>
                ''')
            
            elif (req.POST['pw1'] or req.POST['pw2']) != "":
                user.password = make_password(req.POST['pw1'])
                
            user.adress = req.POST['adress7']
            user.nickname = req.POST['nick']
            user.contact = req.POST['cont']

            user.save()

            return HttpResponse(f'''
                <script>
                    alert("변경되었습니다.");
                    location.href="/whitevalley/user/mypage/"
                </script>
            ''')
        except: 
            return HttpResponse(f'''
            <script>
                alert("모든 주소값을 기입해주세요.");
                history.back();
            </script>
        ''')


    return render(req, 'mypage_modify.html', context)

    
    

    


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