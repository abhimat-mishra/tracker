from django.db import models

# Create your models here.
class Actions(models.Model):
    date=models.DateField()
    time=models.TimeField()
    task=models.CharField(max_length=60)

    def __str__(self):
        return f"Did '{self.task}' at {self.time} on {self.date}"