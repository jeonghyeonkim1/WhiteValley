from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def find_pw(request):
    return render(request,'find_pw.html')

def magazine_list(request):
    return render(request, 'm_list.html')

# 이거 ui설계용이므로 삭제 필수
def magazine_detail(request):
    return render(request, 'm_detail.html')

# def magazine_detail(request, pk):
#     return render(request, 'm_detail.html', pk)
