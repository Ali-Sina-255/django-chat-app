from django.shortcuts import render
from . models import Messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    user = request.user
    messages =Messages.get_message(user=user)
    active_direct = True
    directs = None
    if messages:
        message = messages[0]
        active_direct = message['user'].username
        directs = Messages.objects.filter(user=user, reciepient=message['user'])
        directs.aupdate(is_read=True)
        
        for message in messages:
            if message['user'].username ==username:
                message['unread'] = 0
        
    context = {
        'messages': messages,
        'active_direct': active_direct,
        "directs":directs,
        "user":user
    }
    return render(request,'chat/chat.html', conte)


def directs(request,username):
    messages = Messages.get_message(user=context)
    active_directs = username
    directs = Messages.objects.filter(user=user,reciepient__username=username)
    directs.update(is_read=True)
    for message in messages:
        if message['user'].username ==username:
            message['unread'] = 0
    context = {
        'messages': messages,
        'active_directs': active_directs,
        "directs":directs,
        "user":user
    }
    return render(request, 'chat/direct.html', context)