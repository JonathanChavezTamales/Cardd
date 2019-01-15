from django.db import models

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    company = models.CharField(max_length=40)
    phone = models.CharField(max_length=15, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    isPublic = models.BooleanField(default=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'
