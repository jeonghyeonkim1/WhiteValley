from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator
from cs.models import Board

# 공지사항 페이지
def notice_write(req):
    if req.method == 'GET':
        context = {
            'session': req.session
        }
        return render(req, 'notice_write.html', context)

    elif req.method == 'POST':
        title = req.POST['title']
        content = req.POST['content']

        notice = Board(title=title, content=content)
        notice.save()
        

        return render(req, 'notice_writeOk.html', {"pk": notice.pk})
        

def notice_detail(req, pk):
    notice = Board.objects.get(pk=pk)
    notice.view_cnt += 1
    notice.save()

    context = {
        'session': req.session,
        'notice': notice
    }
    return render(req, 'notice_detail.html', context)


def notice_list(req):
    all_notices = Board.objects.all().order_by('-id')

    page = int(req.GET.get('p', 1))
    paginator = Paginator (all_notices, 5)
    notices = paginator.get_page(page)

    context = {
        'notices': notices,
        'session': req.session
    }

    return render(req, 'notice_list.html', context)


def notice_update(req, pk):
    if req.method == 'GET':
        notice = Board.objects.get(pk=pk)
        context = {
            'session': req.session,
            'notice': notice
        }

        return render(req, 'notice_update.html', context)

    elif req.method == 'POST':
        title = req.POST['title']
        content = req.POST['content']

        notice = Board.objects.get(pk=pk)
        notice.title = title
        notice.content = content
        notice.save()

        return render(req, 'notice_updateOk.html', {"pk": notice.pk})



def notice_delete(req):
    context = {
        'currentPage': 'c/s'
    }
    return render(req, 'notice_delete.html', context)


# 이벤트 페이지
def event_write(req):
    context = {
        'session': req.session
    }
    return render(req, 'event_write.html', context)


def event_detail(req, pk):
    context = {
        'session': req.session
    }
    return render(req, 'event_detail.html', context)


def event_list(req):
    context = {
        'session': req.session
    }
    return render(req, 'event_list.html', context)


def event_update(req, pk):
    context = {
        'currentPage': 'c/s'
    }
    return render(req, 'event_update.html', context)


def event_delete(req):
    context = {
        'currentPage': 'c/s'
    }
    return render(req, 'event_delete.html', context)


# 1:1문의 페이지
def oto_write(req):
    context = {
        'session': req.session
    }
    return render(req, 'oto_write.html', context)


def oto_detail(req, pk):    # 관리자만 볼 수 있음
    context = {
        'session': req.session
    }
    return render(req, 'oto_detail.html', context)


def oto_list(req):
    context = {
        'session': req.session
    }
    return render(req, 'oto_list.html', context)


def oto_answer(req, pk):
    context = {
        'currentPage': 'c/s'
    }
    return render(req, 'oto_answer.html', context)


# FAQ 페이지
def faq_list(req):
    context = {
        'currentPage': 'c/s'
    }
    return render(req, 'faq_list.html', context)


def sample(req):
    context = {
        'currentPage': 'c/s'
    }
    return render(req, 'sample.html', context)


