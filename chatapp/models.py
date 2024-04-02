from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max,Count


class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='from_user')
    reciepient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='to_user')
    body = models.TextField()
    datatime = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def sender_message(from_user, to_user, body):
        sender_message = Messages(
            user=from_user,  # Because you start the convo
            sender=from_user,  # Because you send  the frist message
            reciepient=to_user,  # Because you getting a message from me to ==>  to_user
            body=body,
            is_read=True
        )

        sender_message.save()
        reciepient_message = Messages(
            user=to_user,
            sender=from_user,
            reciepient=from_user,
            body=body,
            is_read=True
        )
        reciepient_message.save()
        return sender_message
    
    
    def get_message(user):
        users = []
        messages = Messages.objects.filter(user=user).values('reciepient').annotate(last=Max('datatime')).order_by('-last')
        for message in messages:
            users.append(
                {
                    "user":User.objects.get(id=message['reciepient']),
                    "last":message["last"],
                    "unread":Messages.objects.filter(user=user,reciepient__id=message["reciepient"],is_read=False)
                }
            )
        return users