from rest_framework import serializers
from roomapp.models import Room


class RoomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    is_booked = serializers.BooleanField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Room` instance, given the validated data.
        """
        return Room.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Room` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.is_booked = validated_data.get('is_booked', instance.is_booked)
        instance.save()
        return instance
