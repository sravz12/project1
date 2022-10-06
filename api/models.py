from django.db import models
from django.contrib.auth.models import User

class Books(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    publisher=models.CharField(max_length=100)
    qty=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

# class Reviews(models.Model):
#     book=models.CharField(max_length=120)
#     user=models.CharField(max_length=100)
#     comment=models.CharField(max_length=200)
#     rating=models.PositiveIntegerField()
#     created_date=models.DateTimeField(auto_now_add=True)

class Reviews(models.Model):
    book = models.ForeignKey(Books,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    rating = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Carts(models.Model):
    book=models.ForeignKey(Books,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("in-cart","in-cart"),
        ("cancelled","cancelled"),
        ("order-placed","order-placed"),
    )
    status=models.CharField(max_length=120,choices=options,default="in-cart")
    #loclhost:8000/api/v4/products/2/add_cart



