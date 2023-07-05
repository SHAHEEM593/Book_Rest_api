from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
