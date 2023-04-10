from django.db import models

# Create your models here.
class Todo(models.Model):
    sarlavha=models.CharField(max_length=50)
    vaqt=models.TimeField()
    izoh=models.TextField()
    maqsad=models.CharField(max_length=50)
    def __str__(self):
        return self.sarlavha