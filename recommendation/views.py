from django.shortcuts import render

def reviews(request):
    context = {
       'session': request.session
    }

    return render(request, 'reviews.html',context)

def reviews_detail(request):
    context = {
       'session': request.session
    }

    return render(request, 'reviews_detail.html',context)

def tag_reviews(request):
    context = {
       'session': request.session
    }

    return render(request, 'tag_reviews.html',context)

def tag_reviews_detail(request):
    context = {
       'session': request.session
    }

    return render(request, 'tag_reviews_detail.html',context)

def finished(request):
    context = {
       'session': request.session
    }

    return render(request, 'finished.html',context)

def finished_detail(request):
    context = {
       'session': request.session
    }

    return render(request, 'finished_detail.html',context)

def product_reviews(request):
    context = {
       'session': request.session
    }

    return render(request, 'product_reviews.html',context)
