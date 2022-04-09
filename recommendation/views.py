from http.client import HTTPResponse
from django.shortcuts import render
from shop.models import Config
from user.models import User
from cs.models import Board
from order.models import Review
from order.models import R_photo,Order,Review_photo_Upload
from recommendation.models import Product, P_photo,Tag_list
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

    }
   
    
    context['orders'] = Order.objects.filter(user=User.objects.get(id=request.session['user']))
    
        
    review = Review.objects.all()
    if len(review) != 0:
        context['rev_del'] = review
    else:
        context['rev_del'] = '리뷰없음'

    List =[]

    for order in Order.objects.all():
        try:
            List.append([Review.objects.get(order=order), R_photo.objects.filter(review=Review.objects.get(order=order))[0]])
        except:
            pass

    context['reviews'] = List

    page = request.GET.get('page', '1')
    paginator = Paginator(List, 9)  # 페이지당 몇개씩 보여주기
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
            order=Order.objects.get(user=User.objects.get(id=request.session['user']), product=Product.objects.get(id=id)),
            title=title, 
            contents=contents, 
        )
        
        rev.save()

        R_photo(review=rev, photo=f'/static/image/product_review/{uploadedFile.name}').save()

        return render(request, 'product_reviews_ok.html', {"pk": rev.pk})

        # return render(request, 'product_reviews_ok.html', {"pk": rev.pk})

# 리뷰 업데이트
def product_reviews_update(request, pk):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        
    }

    if request.method == 'GET':
        try:
            context['review'] =  Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Http404('해당 리뷰를 찾을 수 없습니다.')   
        return render(request, 'product_reviews_update.html', context)

    elif request.method == 'POST':
        title = request.POST['title']
        contents = request.POST['contents']
        
        review = Review.objects.get(pk=pk)
        review.title = title
        review.contents = contents
        review.save()

    return render(request, 'product_reviews_update_ok.html',{'pk':review.pk})

# 리뷰 디테일
def reviews_detail(request,pk):
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        'review' : review
    }

    try:
        review = Review.objects.get(pk=pk)

        review.view_cnt += 1
        review.save()
    except Review.DoesNotExist:
        raise Http404('해당 게시글을 찾을 수 없습니다.')

    return render(request, 'reviews_detail.html',context)

# 리뷰 삭제
def product_reviews_delete(request):
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }

    if request.method == 'POST':
        try:
            id = request.POST['id']
            review = Review.objects.get(order=Order.objects.get(id=id))
            review.delete()
        except:
            return HTTPResponse('''
                <script>
                alert('리뷰작성이 완료되지 않았습니다.')
                </script>
            ''')
    

    return render(request, 'product_reviews_delete_ok.html',context)


# 태그 리뷰리스트
def tag_reviews(request):
    all_product_tag = Product.objects.all().order_by('-reg_date')
    page = request.GET.get('page', '1')
    paginator = Paginator(all_product_tag, 9)  # 페이지당 몇개씩 보여주기
    page_obj = paginator.get_page(page)
    # tag_list = Tag_list.objects.get(product=Product.objects.get(user=User.objects.get(id=request.session['user'])))
    
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        'question_list': page_obj,
        'tag_product' : page_obj
        
    }

    return render(request, 'tag_reviews.html',context)

# 태그 리뷰 디테일
def tag_reviews_detail(request,pk):
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping'
    }
    tag_product = Product.objects.get(pk=pk)
    
    tag_product.save()
    context['tag_product'] = tag_product


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
        'products' : page_obj,
        
    }
        
    return render(request, 'finished.html',context)


# 완성품 디테일
def finished_detail(request,pk):
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',

    }
    
    product = Product.objects.get(pk=pk)
    product.view_cnt += 1
    product.save()
    
    context['product'] = product


    return render(request, 'finished_detail.html',context)


   
          

    