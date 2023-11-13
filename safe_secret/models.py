from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Secret(models.Model):
    hash = models.CharField(max_length=64, verbose_name='Хэш')
    ciphertext = models.TextField(verbose_name='Зашифрованный текст')
    link = models.CharField(max_length=250, verbose_name='Ссылка')
    lifetime = models.PositiveSmallIntegerField(verbose_name='Время жизни')
    code_frase = models.BooleanField(default=True, **NULLABLE)

    def __str__(self):
        return f'Секрет {self.pk}'

    class Meta:
        verbose_name = 'Секрет'
        verbose_name_plural = 'Секреты'
