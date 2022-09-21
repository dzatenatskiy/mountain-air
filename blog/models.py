from django.db import models

class FeedBack(models.Model):
    name = models.CharField(max_length=40, verbose_name='Имя:')
    phone = models.CharField(max_length=40, verbose_name='Телефон:')
    text = models.TextField(max_length=200, verbose_name='Ваше сообщение:')

    def __str__(self):
        return self.phone
