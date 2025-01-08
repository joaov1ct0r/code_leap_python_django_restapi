from django.db import models
# from django.db.models import Manager


class Career(models.Model):
    username = models.CharField(max_length=50)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=70)
    content = models.TextField()

    # objects: Manager = models.Manager()

    def __str__(self):
        return self.title