from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Secret(models.Model):
    code_phrase = models.CharField(max_length=64, verbose_name='Хэш', **NULLABLE)
    ciphertext = models.TextField(verbose_name='Зашифрованный текст')
    link = models.CharField(max_length=250, verbose_name='Ссылка', **NULLABLE)
    lifetime = models.PositiveSmallIntegerField(verbose_name='Время жизни')
    is_code_phrase = models.BooleanField(default=False)
    time_to_delete = models.DateTimeField(verbose_name='время удаления', **NULLABLE)

    def __str__(self):
        return f'Секрет {self.pk}'

    class Meta:
        verbose_name = 'Секрет'
        verbose_name_plural = 'Секреты'
