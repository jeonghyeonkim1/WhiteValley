from django.shortcuts import render
from shop.models import Config
from user.models import User
from cs.models import Board
from order.models import Review
from order.models import R_photo
from . import models
from django.core.paginator import Paginator
from math import ceil
from django.http import Http404



def reviews(request):
    all_review = Review.objects.all().order_by('-reg_date')
    all_photo = R_photo.objects.all()
    page = request.GET.get('page', '1')
    paginator = Paginator(all_review, 8)  # 페이지당 몇개씩 보여주기
    page_obj = paginator.get_page(page)
    
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        'question_list': page_obj,
        'reviews': all_review,
        'r_photo': all_photo,
        
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
    all_board = Board.objects.all()
    page = request.GET.get('page', '1')
    paginator = Paginator(all_board, 9)  # 페이지당 몇개씩 보여주기
    page_obj = paginator.get_page(page)
    
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        'question_list': page_obj,
        'boards' : page_obj
        
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
    all_board = Board.objects.all()
    page = request.GET.get('page', '1')
    paginator = Paginator(all_board, 9)  # 페이지당 몇개씩 보여주기
    page_obj = paginator.get_page(page)
    
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        'question_list': page_obj,
        'boards' : page_obj
        
    }
        

    

    return render(request, 'finished.html',context)

def finished_detail(request):
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }

    return render(request, 'finished_detail.html',context)

# 리뷰작성
def product_reviews(request):
    context = {
    'session': request.session,
    'config': Config.objects.get(id=1),
    'currentpage': 'shopping',
    }
    context['user'] = User.objects.get(id=request.session['user'])
    
    if request.method == 'GET':
        return render(request, 'product_reviews.html',context)
    
    elif request.method == 'POST':
        order = request.POST['order']
        photo = request.POST['photo']
        

        r_photo = R_photo(order = order, photo = photo)
        r_photo.save()  # INSERT 발생
    return render(request, 'product_reviews.html',{'pk':r_photo.pk})
          

    
