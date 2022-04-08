from django.shortcuts import render
from shop.models import Config
from user.models import User
from cs.models import Board
from order.models import Review
from order.models import R_photo,Order,Review_photo_Upload
from recommendation.models import Product, P_photo
from . import models
from django.core.paginator import Paginator
from math import ceil
from django.http import Http404, HttpResponse
import re

# 리뷰 리스트
def reviews(request):
    
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        'R_photo' : R_photo.objects.filter(review=Review.objects.all())
    }
        
    # List =[]

    # for order in Order.objects.all():
    #     try:
    #         List.append([Review.objects.get(order=order), R_photo.objects.filter(order=Review.objects.get(order=order))[0]])
    #     except:
    #         pass

    # context['reviews'] = List
    all_review = R_photo.objects.filter(review=Review.objects.all())
    page = request.GET.get('page', '1')
    paginator = Paginator(all_review, 9)  # 페이지당 몇개씩 보여주기
    page_obj = paginator.get_page(page)
    context['question_list'] = page_obj
    
    return render(request, 'reviews.html',context)

# 리뷰작성
def product_reviews(request,id):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        'product' : Product.objects.get(id=id),
    }
    context['user'] = User.objects.get(id=request.session['user'])
    if request.method == 'GET':
        return render(request, 'product_reviews.html', context)

    elif request.method == 'POST':
        title = request.POST['title']
        contents = request.POST['contents']
        uploadedFile = request.FILES["uploadedFile"]

        

        if len(re.findall(r'\W | [^.]', uploadedFile.name)) > 0:
            return HttpResponse(f'''
                <script>
                    alert("파일 이름에 특수문자가 포함되어 있습니다!");
                    history.back();
                </script>
            ''')
        Review_photo_Upload(title=uploadedFile.name, photo=uploadedFile).save()

        rev = Review(
            order=Order.objects.get(user=User.objects.get(id=request.session['user']),product=Product.objects.get(id=id)),
            title=title, 
            contents=contents, 
        )
        
        rev.save()
        # R_photo(rev=rev, photo=f'/static/image/product_review/{uploadedFile.name}').save()

        return render(request, 'product_reviews_ok.html', {"pk": rev.pk})

        # return render(request, 'product_reviews_ok.html', {"pk": rev.pk})

# 리뷰 업데이트
def product_reviews_update(request):
    context = {
    'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        
    }

    return render(request, 'product_reviews_update.html',context)

# 리뷰 디테일
def reviews_detail(request):
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }

    return render(request, 'reviews_detail.html',context)

# 리뷰 삭제
def product_reviews_delete(request):
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }

    # order 에서 product 에 review 삭제 경로

    return render(request, 'product_reviews_delete_ok.html',context)


# 태그 리뷰리스트
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

# 태그 리뷰리스트
def tag_reviews_detail(request):
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }

    return render(request, 'tag_reviews_detail.html',context)

# 완성품 리스트
def finished(request):
    all_product = Product.objects.all().order_by('-reg_date')
    page = request.GET.get('page', '1')
    paginator = Paginator(all_product, 9)  # 페이지당 몇개씩 보여주기
    page_obj = paginator.get_page(page)
    
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        'question_list': page_obj,
        'products' : page_obj
        
    }
        

    

    return render(request, 'finished.html',context)

# 완성품 디테일
def finished_detail(request):
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }

    return render(request, 'finished_detail.html',context)


   
          

    