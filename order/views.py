from django.shortcuts import render

# Create your views here.
def order(request):
    context = {
        'currentPage' : 'order'
    }
    return render(request, 'order.html',context)

def order_des(request):
    context ={
        'currentPage' : 'order_des'
    }
    return render(request, 'order_des.html',context)

def custom1(request):
   
    return render(request, 'custom1.html')

    
def custom2(request):
   
    return render(request, 'custom2.html')

def customend(request):
   
    return render(request, 'customend.html')