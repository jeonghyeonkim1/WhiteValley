from django.shortcuts import render


# 공지사항 페이지
def notice_write(req):
    context = {
        'currentPage': 'c/s'
    }
    return render(req, 'notice_write.html', context)
    

def notice_detail(req, pk):
    context = {
        'currentPage': 'c/s'
    }
    return render(req, 'notice_detail.html', context)


def notice_list(req):
    context = {
        'currentPage': 'c/s'
    }
    return render(req, 'notice_list.html', context)


def notice_update(req, pk):
    context = {
        'currentPage': 'c/s'
    }
    return render(req, 'notice_update.html', context)


def notice_delete(req):
    context = {
        'currentPage': 'c/s'
    }
    return render(req, 'notice_delete.html', context)


# 이벤트 페이지
def event_write(req):
    context = {
        'currentPage': 'c/s'
    }
    return render(req, 'event_write.html', context)


def event_detail(req, pk):
    context = {
        'currentPage': 'c/s'
    }
    return render(req, 'event_detail.html', context)


def event_list(req):
    context = {
        'currentPage': 'c/s'
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
        'currentPage': 'c/s'
    }
    return render(req, 'oto_write.html', context)


def oto_detail(req, pk):    # 관리자만 볼 수 있음
    context = {
        'currentPage': 'c/s'
    }
    return render(req, 'oto_detail.html', context)


def oto_list(req):
    context = {
        'currentPage': 'c/s'
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


