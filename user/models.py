from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    profile_pic = models.ImageField(
        upload_to="user/media/profile_pics",
        )
    isPremium = models.BooleanField(default=False)

    def __str__(self):
        return self.email
