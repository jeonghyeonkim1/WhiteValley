from django.shortcuts import render

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


def oto_write(req):
    context = {
        'currentPage': 'c/s'
    }
    return render(req, 'oto_write.html', context)


def oto_list(req):
    context = {
        'currentPage': 'c/s'
    }
    return render(req, 'oto_list.html', context)


def faq_list(req):
    context = {
        'currentPage': 'c/s'
    }
    return render(req, 'faq_list.html', context)


