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


def reviews(request):
    
    
    
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        'orders' : Order.objects.filter(user=User.objects.get(id=request.session['user'])),
    }

    List =[]

    for order in Order.objects.all():
        try:
            List.append([Review.objects.get(order=order), R_photo.objects.filter(order=Review.objects.get(order=order))[0]])
        except:
            pass

    context['reviews'] = List

    page = request.GET.get('page', '1')
    paginator = Paginator(List, 8)  # 페이지당 몇개씩 보여주기
    page_obj = paginator.get_page(page)
    context['question_list'] = page_obj
    
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
    all_product = Product.objects.all()
    all_p_photo = P_photo.objects.all()
    page = request.GET.get('page', '1')
    paginator = Paginator(all_product, 9)  # 페이지당 몇개씩 보여주기
    page_obj = paginator.get_page(page)
    
    context = {
       'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'shopping',
        'question_list': page_obj,
        'products' : all_product
        
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
        order = Order.objects.get(user=User.objects.get(id=request.session['user']))
        title = request.POST['title']
        contents = request.POST['contents']
        uploadedFile = request.FILES["uploadedFile"]


        if len(re.findall(r'[^a-z | 0-9 | . | " " | ( | )]', uploadedFile.name)) > 0:
            return HttpResponse(f'''
                <script>
                    alert("파일 이름에 특수문자가 포함되어 있습니다!");
                    history.back();
                </script>
            ''')
        photo = Review_photo_Upload(title=uploadedFile.name, photo=uploadedFile)
        photo.save()

        rev = Review(
            order=order, 
            title=title, 
            contents=contents, 
        )
        
        rev.save()

        return render(request, 'product_reviews_ok.html', {"pk": rev.pk})
        # R_photo(rev=rev, photo=f'/static/image/product_review/{photo.title}').save()

        # return render(request, 'product_reviews_ok.html', {"pk": rev.pk})


   
    # context = {
    # 'session': request.session,
    # 'config': Config.objects.get(id=1),
    # 'currentpage': 'shopping',
    # # 'order' : Order.objects.filter(user=User.objects.get(id=request.session['user'])),
    # 'product' : Product.objects.get(id=id),
    # 'user' : User.objects.get(id=request.session['user'])
    # }
    # # context['user'] = User.objects.get(id=request.session['user'])
    
    # if request.method == 'GET':
    #     return render(request, 'product_reviews.html', context)

    # elif request.method == 'POST':
    #     order = Order.objects.get(user=User.objects.get(id=request.session['user']))
    #     title = request.POST['title']
    #     contents = request.POST['contents']
    #     uploadedFile = request.FILES['uploadedFile']

    #     if len(re.findall(r'[^a-z | 0-9 | . | " " | ( | )]', uploadedFile.name)) > 0:
    #         return HttpResponse(f'''
    #             <script>
    #                 alert("파일 이름에 특수문자가 포함되어 있습니다!");
    #                 history.back();
    #             </script>
    #         ''')

    #     # uploadedFileName = re.sub(r"\W | [^.] | [^_]", "", uploadedFile.name.replace(" ", "_").replace("(", "").replace(")", ""))
    #     # Review_photo_Upload(uploadedFileName=uploadedFileName , photo=uploadedFile).save()
    #     photo = Review_photo_Upload(title=uploadedFile.name , photo=uploadedFile)
    #     photo.save()
    #     rev = Review(
    #         order=order, 
    #         title=title, 
    #         contents=contents, 
    #         # photo=uploadedFile
    #         )
    #     rev.save()

    #     R_photo(rev=rev, photo=f'/static/image/product_review/{photo.title}').save()

    #     context['pk'] = rev.pk
    #     return render(request, 'product_reviews_ok.html',context)
    
   
          

    