from rest_framework import serializers
from .models import Form


class FormSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Form
        fields = ("id", "title", "user", "userId", "formId", "created_at")
