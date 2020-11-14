from django.db import models
import string
import random

#function to generate unquie code for the room
def generate_unique_code():
    length = 6

    while True :
        code = ''.join(random.choices(string.ascii_uppercase , k = length))
        if Room.objects.filter(code=code).count() == 0 :
            break

    return code

#class room to set data base for room and defin types and fields using django.db models
class Room (models.Model):
    code = models.CharField(max_length=8 , null=False , default='' , unique=True)
    host = models.CharField(max_length=50 , null=False , default='' , unique=True)
    gust_can_pause = models.BooleanField(null=False , default=False)
    votes_to_skip = models.IntegerField(null=False , default=2 )
    created_at = models.DateTimeField(auto_now_add=True)
