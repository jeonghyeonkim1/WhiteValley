from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.models import User
from cs.models import Board
from shop.models import Config, Co_account
import datetime
from django.core.paginator import Paginator

# HOME --------------------------------------------------------------------------------
def home(req):
    context = {
        'cookies': req.COOKIES,
        'session': req.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'home',
        'notices': Board.objects.filter(tag="공지사항").order_by("-reg_date")[:12],
        'faqs': Board.objects.filter(tag="FAQ").order_by("-reg_date")[:4],
        'magazines': Board.objects.filter(tag="매거진").order_by("-reg_date")[:4]
    }

    cookie_name = 'visited'
    cookie_value = True

    context['cookie_name'] = cookie_name
    context['cookie_value'] = cookie_value

    res = render(req, 'home.html', context)

    res.set_cookie(
        key=cookie_name,
        value=cookie_value,
        expires=360
    )

    return res


# CART ----------------------------------------------------------------------------------
def cart(req):
    context = {
        'session': req.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'cart'
    }

    return render(req, 'cart.html', context)


# ADMIN -----------------------------------------------------------------------------------
def admin(req):
    context = {
        'session': req.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'admin',
    }

    if req.method == "GET":
        try:
            if req.session['admin']:
                return render(req, 'admin.html', context)
            else:
                return HttpResponse(f'''
                    <script>
                        alert("권한이 없습니다!!");
                        location.href='/whitevalley/';
                    </script>
                ''')
            
        except:
            return HttpResponse(f'''
                <script>
                    alert("관리자 계정의 로그인이 필요합니다.");
                    location.href='/whitevalley/login/';
                </script>
            ''')

    elif req.method == "POST":
        config = Config.objects.get(id=1)

        config.name = req.POST['name']
        config.ceo = req.POST['ceo']
        config.email = req.POST['email']
        config.number = req.POST['number']
        config.address = req.POST['address']
        config.site_name = req.POST['site_name']
        config.sale_time = req.POST['sale_time']
        config.lunch_time = req.POST['lunch_time']
        config.holiday = req.POST['holiday']

        config.save()

        return redirect('/whitevalley/admin/')


def admin_member(req):
    context = {
        'session': req.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'admin'
    }
    
    if req.method == "GET":
        try:
            if req.session['admin']:
                context['date'] = "전체"
                context['order'] = "가입일순"
                context['users'] = User.objects.all().order_by('-reg_date')
                page = int(req.GET.get('page', 1))
            else:
                return HttpResponse(f'''
                    <script>
                        alert("권한이 없습니다!!");
                        location.href='/whitevalley/';
                    </script>
                ''')
            
        except:
            return HttpResponse(f'''
                <script>
                    alert("관리자 계정의 로그인이 필요합니다.");
                    location.href='/whitevalley/';
                </script>
            ''')
    
    elif req.method == "POST":
        date_filter = req.POST['date_filter']
        context['date'] = date_filter
        order_filter = req.POST['order_filter']
        context['order'] = order_filter
        

        if date_filter == "전체":
            datepicker1 = "2000-01-01"
            datepicker2 = datetime.datetime.now().date() + datetime.timedelta(days=1)
        elif date_filter == "오늘":
            datepicker1 = datetime.datetime.now().date()
            datepicker2 = datetime.datetime.now().date() + datetime.timedelta(days=1)
        elif date_filter == "1주일":
            datepicker1 = datetime.datetime.now().date() + datetime.timedelta(days=-7)
            datepicker2 = datetime.datetime.now().date() + datetime.timedelta(days=1)
        elif date_filter == "1개월":
            datepicker1 = datetime.datetime.now().date() + datetime.timedelta(days=-30)
            datepicker2 = datetime.datetime.now().date() + datetime.timedelta(days=1)
        elif date_filter == "3개월":
            datepicker1 = datetime.datetime.now().date() + datetime.timedelta(days=-90)
            datepicker2 = datetime.datetime.now().date() + datetime.timedelta(days=1)
        elif date_filter == "직접선택":
            datepicker1 = req.POST['datepicker1']
            context['datepicker1_value'] = datepicker1
            datepicker2 = req.POST['datepicker2']
            context['datepicker2_value'] = datepicker2
                

        if order_filter == "가입일순":
            context['order'] = "가입일순"
            context['users'] = User.objects.filter(reg_date__range=[datepicker1, datepicker2]).order_by('-reg_date')
        elif order_filter == "ID순":
            context['order'] = "ID순"
            context['users'] = User.objects.filter(reg_date__range=[datepicker1, datepicker2]).order_by('-id')
        elif order_filter == "닉네임순":
            context['order'] = "닉네임순"
            context['users'] = User.objects.filter(reg_date__range=[datepicker1, datepicker2]).order_by('-nickname')
        elif order_filter == "연락처순":
            context['order'] = "연락처순"
            context['users'] = User.objects.filter(reg_date__range=[datepicker1, datepicker2]).order_by('-contact')

    # 한 페이지에 글 몇개?
    per_page = int(req.session.get('per_page', 5))

    # 현재 몇 페이지?
    page = int(req.GET.get('page', 1))

    # 한페이지당 per_page 씩
    paginator = Paginator(context['users'], per_page)

    # Page는 pagintor에 대한 정보도 담고 있음
    page_obj = paginator.get_page(page)

    write_pages = int(req.session.get('write_pages', 10))
    start_page = (int((page_obj.number - 1) / write_pages) * write_pages) + 1
    end_page = start_page + write_pages - 1

    if end_page >= paginator.num_pages:
        end_page = paginator.num_pages

    context['users'] = page_obj
    context['write_pages'] = write_pages
    context['start_page'] = start_page
    context['end_page'] = end_page
    context['page_range'] = range(start_page, end_page + 1)
            
    return render(req, 'admin_member.html', context)


def member_delete(req, id):
    User.objects.get(id=id).delete()

    return HttpResponse(f'''
        <script>
            alert("해당 유저가 회원탈퇴 처리되었습니다!!");
            location.href = '/whitevalley/admin/member/'
        </script>
    ''')


def admin_point(req):
    context = {
        'session': req.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'admin',
    }

    if req.method == "GET":
        try:
            if req.session['admin']:
                return render(req, 'admin_point.html', context)
            else:
                return HttpResponse(f'''
                    <script>
                        alert("권한이 없습니다!!");
                        location.href='/whitevalley/';
                    </script>
                ''')
            
        except:
            return HttpResponse(f'''
                <script>
                    alert("관리자 계정의 로그인이 필요합니다.");
                    location.href='/whitevalley/login/';
                </script>
            ''')

    elif req.method == "POST":
        config = Config.objects.get(id=1)

        config.tag_show = req.POST['tag_expose']
        config.sign_point = req.POST['sign_point']
        config.return_point = req.POST['return_point']
        config.review_point = req.POST['review_point']
        config.best_point = req.POST['best_point']
        config.min_amount = req.POST['min_amount']
        config.max_point = req.POST['max_point']

        config.save()

        return redirect('/whitevalley/admin/point/')


def admin_account(req):
    context = {
        'session': req.session,
        'config': Config.objects.get(id=1),
        'accounts': Co_account.objects.all(),
        'currentpage': 'admin',
    }

    if req.method == "GET":
        try:
            if req.session['admin']:
                return render(req, 'admin_account.html', context)
            else:
                return HttpResponse(f'''
                    <script>
                        alert("권한이 없습니다!!");
                        location.href='/whitevalley/';
                    </script>
                ''')
            
        except:
            return HttpResponse(f'''
                <script>
                    alert("관리자 계정의 로그인이 필요합니다.");
                    location.href='/whitevalley/login/';
                </script>
            ''')

    elif req.method == "POST":

        return redirect('/whitevalley/admin/account/')


def account_add(req):
    bank = req.POST['bank']
    depositer = req.POST['depositer']
    number = req.POST['number']

    try:
        Co_account.objects.get(bank=bank)
        return HttpResponse(f'''
            <script>
                alert("{bank}계좌가 이미 존재합니다!");
                location.href = '/whitevalley/admin/account/'
            </script>
        ''')
    
    except:
        Co_account(bank=bank, depositer=depositer, number=number).save()
        return HttpResponse(f'''
            <script>
                alert("계좌가 추가되었습니다!");
                location.href = '/whitevalley/admin/account/'
            </script>
        ''')
        


def account_delete(req, bank):
    Co_account.objects.get(bank=bank).delete()

    return HttpResponse(f'''
        <script>
            alert("{bank} 계좌가 삭제되었습니다!!");
            location.href = '/whitevalley/admin/account/'
        </script>
    ''')