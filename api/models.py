from django.db import models

class Books(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    publisher=models.CharField(max_length=100)
    qty=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

class Reviews(models.Model):
    book=models.CharField(max_length=120)
    user=models.CharField(max_length=100)
    comment=models.CharField(max_length=200)
    rating=models.PositiveIntegerField()
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment



