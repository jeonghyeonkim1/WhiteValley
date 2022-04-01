from django.http import HttpResponse
from django.shortcuts import render
from user.models import User
from shop.models import Config

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
    try:
        if req.session['admin']:
            context = {
                'session': req.session,
                'config': Config.objects.get(id=1),
                'currentpage': 'admin',
            }
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
                alert("로그인이 필요합니다.");
                location.href='/whitevalley/login/';
            </script>
        ''')

def admin_customer(req):
    try:
        if req.session['admin']:
            context = {
                'session': req.session,
                'config': Config.objects.get(id=1),
                'currentpage': 'admin',
            }

            context['users'] = User.objects.all()
            return render(req, 'admin_customer.html', context)
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
                alert("권한이 없습니다!!");
                location.href='/whitevalley/';
            </script>
        ''')

    