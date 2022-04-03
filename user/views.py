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

            user = User.objects.get(email = email)
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
                    el = email.split("@")[0] + str(cnt + 1)
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
                    location.href = '/whitevalley/'
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
        return render(request,'find_pw.html', context)

    elif request.method == ('POST'):
        email = request.POST['email']

        if (User.objects.filter(email=email).exists()) == False:
            context['error'] = '이메일이 없습니다.'

    return render(request, 'find_pw.html', context)
        


def chpw(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'login'
    }

    # user = User.objects.get(email = email)
    # try :
    #     pk = user.objects.get(pk=pk)
    # except User.DoesNotExist:
    #     raise Http404('유저정보를 찾을수 없습니다.')
    
    # new_password = request.POST['password']
    # re_password = request.POST['re_password']

    # res_data = {}

    # if not(new_password and re_password):
    #     res_data['error'] = '입력 전체 입력해주세요'
    # elif new_password != re_password:
    #     res_data['error'] = '비밀번호가 다릅니다.'
    # else:
    #     user = User(
    #         password = make_password(new_password),
    #     )
    #     user.save()

    if request.method =="GET":
        return render(request, 'chpw.html', context)
    elif request.method =="POST":
        return render(request, 'chpwOk.html', context)




def magazine_list(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'magazine'
    }
    # if request.method == "GET":
    return render(request, 'm_list.html', context)
    # elif request.method == "POST":
    #     return render(request, 'm_list.html', context)


    # 그냥 게시

# def magazine_per_page(request):
#     page = int(request.POST['page'])
#     per_page = int(request.POST['per_page'])
#     request.session['per_page'] = per_page

#     return redirect(f'/magazine/list/?page={page}')
    

# 이거 ui설계용이므로 삭제 필수
# def magazine_detail(request):

#     context = {
#         'session': request.session,
#         'config': Config.objects.get(id=1),
#         'currentpage': 'sign'
#     }

#     if request.method =="GET":
#         # try: 
#         #     board = Board.objects.get(pk=pk)
#         # except Board.DoesNotExist:
#         #     raise Http404('게시글을 찾을수 없습니다.')

#         # return render(request, 'board/update.html', {'board': board})
#         return render(request, 'm_update.html', context)
#     elif request.method =="POST":
#         # subject = request.POST['subject']
#         # content = request.POST['content']
        
#         # # 수정 1.읽어오기
#         # board = Board.objects.get(pk=pk)
#         # # 2. 수정
#         # board.subject = subject
#         # board.content = content
#         # # 3. 저장
#         # board.save()

#         # return render(request, 'board/updateOk.html', {"pk" : board.pk})
#         return render(request, 'm_updateOk.html')




def magazine_detail(request, pk):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'magazine'
    }

    try:
        board = Board.objects.get(pk=pk)  # id(pk) 값의 글 읽어오기 . SELECT

        board.view_cnt += 1
        board.save()
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을수 없습니다')

    return render(request, 'm_detail.html', {'board': board}, context)



# 이거 ui설계용이므로 삭제 필수
def magazine_update(request):

    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'magazine'
    }

    return render(request, 'm_update.html', context)

# def magazine_update(request, pk):
#     if request.method == "GET":
#         try:
#             board = Board.objects.get(pk=pk)
#         except Board.DoesNotExist:
#             raise Http404('게시글을 찾을수 없습니다')

#         return render(request, 'm_update.html', {'board': board})
    
#     elif request.method == "POST":
#         subject = request.POST['subject']
#         content = request.POST['content']

#         # 수정
#         board = Board.objects.get(pk=pk)
#         board.subject = subject
#         board.content = content
#         board.save()   # UPDATE

#         return render(request, 'm_updateOk.html', {"pk": board.pk })
#     return render(request, 'm_update.html', pk)

def magazine_write(request):

    if request.method == 'GET':
        context = {
            'session': request.session,
            'config': Config.objects.get(id=1),
            'currentpage': 'magazine'
        }
        return render(request, 'm_write.html', context)

    elif request.method == 'POST':
        user = User.objects.get(id=request.session['admin'])
        tag = request.POST['notice']
        title = request.POST['title']
        content = request.POST['content']

        notice = Board(user=user, title=title, content=content, tag=tag)
        notice.save()
        
        return render(request, 'm_write.html', context)

def magazine_delete(request):

    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'magazine'
    }

    return render(request, 'm_deleteok.html', context)

def mypage(req):
    context = {
        'session': req.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'mypage'
    }

    context['user'] = User.objects.get(id=req.session['user'])

    return render(req, 'mypage.html', context)