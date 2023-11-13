from rest_framework import serializers
from safe_secret.models import Secret


class SecretSerializer(serializers.ModelSerializer):

    class Meta:
        model = Secret
        fields = ['code_phrase', 'lifetime', 'ciphertext', 'link']


class SecretRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Secret
        fields = ['ciphertext']
