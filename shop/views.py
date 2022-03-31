from django.shortcuts import render

def home(req):
    context = {
        'cookies': req.COOKIES,
        'session': req.session
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
    return render(req, 'cart.html')