from django.db import models


# Create your models here.

class HOST_NAME(models.Model):
    namehost = models.CharField(max_length=200, help_text='Введите адрес сайта: ')

    def __str__(self):
        return self.namehost


class INPUT_INF_HOST(models.Model):
    INT_DATA = models.DateTimeField(auto_now_add=True)
    ID_HOST = models.IntegerField()
    ID_USER = models.IntegerField()
    NAME_HOST = models.TextField()
    PORT_HOST = models.IntegerField()

    def __str__(self):
        return self.NAME_HOST
