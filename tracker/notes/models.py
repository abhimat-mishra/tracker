from django.db import models

# Create your models here.
class AddShow(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    note = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.note}"