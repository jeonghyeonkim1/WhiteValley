from django.shortcuts import render
from shop.models import Config

def reviews(request):
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }

    return render(request, 'reviews.html',context)

def reviews_detail(request):
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }

    return render(request, 'reviews_detail.html',context)

def tag_reviews(request):
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }

    return render(request, 'tag_reviews.html',context)

def tag_reviews_detail(request):
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }

    return render(request, 'tag_reviews_detail.html',context)

def finished(request):
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }

    return render(request, 'finished.html',context)

def finished_detail(request):
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }

    return render(request, 'finished_detail.html',context)

def product_reviews(request):
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }

    return render(request, 'product_reviews.html',context)
