from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.models import User
from shop.models import Config, Co_account
import datetime

# HOME --------------------------------------------------------------------------------
def home(req):
    context = {
        'cookies': req.COOKIES,
        'session': req.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'home'
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
        'currentpage': 'admin',
        'now': datetime.datetime.now(),
        'week_ago': datetime.datetime.now() - datetime.timedelta(days=7)
    }
    if req.method == "GET":
        try:
            if req.session['admin']:
                context['users'] = User.objects.all().order_by('-reg_date')
                return render(req, 'admin_member.html', context)
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
        return redirect('/whitevalley/admin/member/')


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