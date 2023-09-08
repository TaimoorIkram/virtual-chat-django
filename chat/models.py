from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Villa(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, default="My New Villa")
    created_by =  models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Room(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, default='My New Room')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    villa = models.ForeignKey(Villa, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return ' by '.join([self.name, self.created_by.username])

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.TextField(null=False)
    send_time = models.DateTimeField(auto_now_add=True)