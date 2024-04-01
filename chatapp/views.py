from django.shortcuts import render
from . models import Messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    user = request.user
    messages = Messages.get_message(user=user)
    active_direct = None
    directs = None

    for message in messages:
        message = messages[0]
        active_direct = message['user'].username
        directs = Messages.objects.filter(user=request.user, reciepient=message['user'])
        directs.update(is_read=True)
        for message in messages:
            if message['user'].username ==active_direct:
                message['unread'] = 0
        
    context = {
        'messages': messages,
        'active_direct': active_direct,
        "directs": directs,
        "user": user
    }
    return render(request, 'chat/home.html', context)


def directs(request, username):
    user = request.user
    messages = Messages.get_message(user=user)
    active_directs = username
    directs = Messages.objects.filter(user=user, reciepient__username=username)
    directs.update(is_read=True)
    for message in messages:
        if message['user'].username == username:
            message['unread'] = 0

    context = {
        'messages': messages,
        'active_directs': active_directs,
        "directs": directs,
        "user": user
    }
    return render(request, 'chat/direct.html', context)


def new_test_user(request,pk):
    pass
    return render(request, 'test/test.html')


def send_message(request):
    pass
    return render(request, 'message/message.html')