from django.shortcuts import render
from shop.models import Config
from user.models import User
from cs.models import Board
from . import models
from django.core.paginator import Paginator
from math import ceil


def reviews(request):
    all_boards = Board.objects.all().order_by('-id')
    write_pages = int(request.session.get('write_pages', 10))
    per_page = int(request.session.get('per_page',5))     # 세션에 세팅값으로 활용 (없으면 5)
    page = int(request.GET.get('page', 1))

    paginator = Paginator(all_boards, per_page)    # 한 페이지당 per_page 씩 보여주는 Paginator 생성
    page_obj = paginator.get_page(page)     # page 는 paginator 에 대한 정보도 담고있다.


    start_page = ((int)((page_obj.number - 1) / write_pages) * write_pages) + 1
    end_page = start_page + write_pages - 1

    if end_page >= paginator.num_pages:
        end_page = paginator.num_pages
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        'boards' : page_obj,    # 현재 page 객체
        # 'count' : all_count,
        'write_pages': write_pages,
        'start_page' : start_page,
        'end_page': end_page,
        'page_range': range(start_page, end_page + 1)
        
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
    all_boards = Board.objects.all().order_by('-id')
    
    write_pages = int(request.session.get('write_pages', 10))
    per_page = int(request.session.get('per_page',5))     # 세션에 세팅값으로 활용 (없으면 5)
    page = int(request.GET.get('page', 1))

    paginator = Paginator(all_boards, per_page)    # 한 페이지당 per_page 씩 보여주는 Paginator 생성
    page_obj = paginator.get_page(page)     # page 는 paginator 에 대한 정보도 담고있다.


    start_page = ((int)((page_obj.number - 1) / write_pages) * write_pages) + 1
    end_page = start_page + write_pages - 1

    if end_page >= paginator.num_pages:
        end_page = paginator.num_pages
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        'boards' : page_obj,    # 현재 page 객체
        # 'count' : all_count,
        'write_pages': write_pages,
        'start_page' : start_page,
        'end_page': end_page,
        'page_range': range(start_page, end_page + 1)
        
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
    context['user'] = User.objects.get(id=request.session['user'])

    if request.method == 'GET':
        return render(request, 'product_reviews.html')
    elif request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        content = request.POST['content']

        b = Board(name = name, subject = subject, content = content)
        b.save()
    return render(request, 'product_reviews.html',context)
