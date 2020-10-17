from rest_framework import serializers
from new.models import camera

class camera_deteil_serializer(serializers.ModelSerializer):
    class Meta:
        model = camera
        fields = "__all__"


class camera_list_serializer(serializers.ModelSerializer):
    class Meta:
        model = camera
        fields = ('id', 'cam_id', 'cam_time')
