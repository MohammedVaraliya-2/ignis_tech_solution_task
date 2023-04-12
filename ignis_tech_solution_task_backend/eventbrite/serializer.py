from rest_framework import serializers
from .models import Event

class ReactEventSerializer(serializers.ModelSerializer):

    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'event_name', 'date', 'time', 'location', 'is_liked', 'image', 'image_url']

    def get_image_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.image.url)