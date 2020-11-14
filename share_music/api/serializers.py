#what a this serializers do it will take models and change it to jason
#so the front end will understand it and can render it

from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id','code', 'host' , 'gust_can_pause' ,
                        'votes_to_skip' ,'created_at' )