import re
from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator
from cs.models import Board
from shop.models import Config

# 공지사항 페이지
def notice_write(request):
    if request.method == 'GET':
        context = {
            'session': request.session,
            'config': Config.objects.get(id=1),
            'currentpage': 'cs'
        }
        return render(request, 'notice_write.html', context)

    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        notice = Board(title=title, content=content)
        notice.save()
        

        
        return render(request, 'notice_writeOk.html', {"pk": notice.pk})

def notice_detail(request, pk):
    notice = Board.objects.get(pk=pk)
    notice.view_cnt += 1
    notice.save()

    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'cs',
        'notice': notice
    }
    return render(request, 'notice_detail.html', context)


def notice_list(request):
    keyword = request.GET.get('keyword')
    
    if keyword:
        all_notices = Board.objects.filter(title__contains=keyword).order_by('-reg_date')
    else:
        all_notices = Board.objects.all().order_by('-reg_date')

    page = int(request.GET.get('page', 1))
    paginator = Paginator (all_notices, 5)
    notices = paginator.get_page(page)

    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'cs',
        'notices': notices,
        'all_notices': all_notices,
        # 'keyword': keyword
    }
        

    return render(request, 'notice_list.html', context)


def notice_update(request, pk):
    if request.method == 'GET':
        notice = Board.objects.get(pk=pk)
        context = {
            'session': request.session,
            'config': Config.objects.get(id=1),
            'currentpage': 'cs',
            'notice': notice
        }

        return render(request, 'notice_update.html', context)

    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        notice = Board.objects.get(pk=pk)
        notice.title = title
        notice.content = content
        notice.save()

        return render(request, 'notice_updateOk.html', {"pk": notice.pk})


def notice_delete(request):
    if request.method == 'POST':
        id = request.POST['id']
        notice = Board.objects.get(id=id)
        notice.delete()

    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'cs'
    }
    return render(request, 'notice_deleteOk.html', context)


# 이벤트 페이지
def event_write(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'cs'
    }
    return render(request, 'event_write.html', context)


def event_detail(request, pk):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'cs'
    }
    return render(request, 'event_detail.html', context)


def event_list(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'cs'
    }
    return render(request, 'event_list.html', context)


def event_update(request, pk):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'cs'
    }
    return render(request, 'event_update.html', context)


def event_delete(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'cs'
    }
    return render(request, 'event_delete.html', context)


# 1:1문의 페이지
def oto_write(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'cs'
    }
    return render(request, 'oto_write.html', context)


def oto_detail(request, pk):    # 관리자만 볼 수 있음
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'cs'
    }
    return render(request, 'oto_detail.html', context)


def oto_list(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'cs'
    }
    return render(request, 'oto_list.html', context)


def oto_answer(request, pk):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'cs'
    }
    return render(request, 'oto_answer.html', context)


# FAQ 페이지
def faq_list(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'cs'
    }
    return render(request, 'faq_list.html', context)


def sample(request):
    context = {
        'session': request.session,
        'config': Config.objects.get(id=1),
        'currentpage': 'cs'
    }
    return render(request, 'sample.html', context)


