from django.db import models

class Books(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    publisher=models.CharField(max_length=100)
    qty=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name



