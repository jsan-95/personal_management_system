# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = CustomUser
        fields = '__all__'

    def get_image_url(self, obj):
        try:
            avatar_url = '/' + obj.avatar.url
        except Exception:
            avatar_url = ''

        return avatar_url
