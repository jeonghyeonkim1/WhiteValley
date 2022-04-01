from django.shortcuts import render
from .models import Config

def home(req):
    context = {
        'cookies': req.COOKIES,
        # 모든 페이지에 적용해주세요 ----------------------
        'session': req.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'home'
        # -----------------------------------------------
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

def cart(req):
    context = {
        'session': req.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'cart'
    }

    return render(req, 'cart.html', context)