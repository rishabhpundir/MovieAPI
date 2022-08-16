from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.Serializer):
    # model = Movie
    # fields = ['id', 'name', 'genre', 'release', 'description', 'active'] 

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    genre = serializers.CharField()
    release = serializers.IntegerField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.release = validated_data.get('release', instance.release)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short!')
        else:
            return value
