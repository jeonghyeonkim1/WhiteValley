from contextlib import redirect_stderr
from django.shortcuts import render

# Create your views here.
def order(request):
    return render(request,'order.html')

def order_des(request):
   
    return render(request, 'order_des.html')

def custom1(request):
   
    return render(request, 'custom1.html')

    
def custom2(request):
   
    return render(request, 'custom2.html')

def customend(request):
   
    return render(request, 'customend.html')

def payment(request):
   
    return render(request, 'payment.html')