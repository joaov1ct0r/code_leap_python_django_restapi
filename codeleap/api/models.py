from django.db import models

class Post(models.Model):
    objects = models.Manager()

    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=70)
    content = models.TextField()

    def __str__(self):
        return self.title