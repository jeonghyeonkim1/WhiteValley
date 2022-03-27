from django.shortcuts import render


def home(req):
    context = {
        'currentPage': 'home'
    }

    return render(req, 'home.html', context)
