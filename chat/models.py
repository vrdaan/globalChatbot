from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Message(models.Model):
    contact = models.ForeignKey(
        User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    room = models.CharField(max_length = 50,default='room',)

    def __str__(self):
        return self.contact.username

    def last_30_messages(roomName):
        return Message.objects.filter(room = roomName)
