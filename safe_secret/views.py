import secrets

from rest_framework import generics, status
from rest_framework.response import Response

from safe_secret.models import Secret
from safe_secret.serializers import SecretSerializer, SecretRetrieveSerializer
from safe_secret.services import sha256_hash, Encryptor, make_link


class SecretCreateAPIViev(generics.CreateAPIView):
    serializer_class = SecretSerializer
    queryset = Secret.objects.all()

    def perform_create(self, serializer):
        secret = serializer.save()
        text = serializer.validated_data.get('ciphertext')
        secret.ciphertext = Encryptor().encrypt_text(text)
        code_phrase = serializer.validated_data.get('code_phrase')
        if code_phrase:
            secret.code_phrase = sha256_hash(code_phrase)
            secret.is_code_phrase = True
        else:
            secret.code_phrase = secrets.token_hex(32)
        link = make_link(secret.code_phrase)
        secret.link = link
        secret.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        link = response.data.get('link')
        return Response({'link': link}, status=status.HTTP_201_CREATED)


class SecretRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SecretRetrieveSerializer
    queryset = Secret.objects.all()

    def retrieve(self, request, *args, **kwargs):
        code_phrase = self.kwargs.get('code_phrase')
        try:
            secret = Secret.objects.get(code_phrase=code_phrase)
        except Secret.DoesNotExist:
            return Response({'error': 'Такого объекта не существует. Вы воспользовались неверной ссылкой, '
                                      'либо данные по ссылке уже были просмотрены и удалены.'},
                            status=status.HTTP_404_NOT_FOUND)

        if secret.is_code_phrase is True:
            code_phrase = request.data.get('code_phrase')
            hashed_phrase = sha256_hash(code_phrase)
            if hashed_phrase != secret.code_phrase:
                return Response({'error': 'Неверная кодовая фраза'}, status=status.HTTP_400_BAD_REQUEST)

        plaintext = Encryptor().decrypt_text(secret.ciphertext)
        serializer = self.get_serializer(data={'ciphertext': plaintext})
        serializer.is_valid(raise_exception=True)

        secret.delete()

        return Response(serializer.data)
