from rest_framework import serializers
from api.models import Reviews
from api.models import Books
from django.contrib.auth.models import User
class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    author=serializers.CharField()
    price=serializers.IntegerField()
    publisher=serializers.CharField()
    qty=serializers.IntegerField()

    def create(self, validated_data):
        return Books.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name=validated_data.get("name")
        instance.author=validated_data.get("author")
        instance.price=validated_data.get("price")
        instance.publisher=validated_data.get("publisher")
        instance.qty=validated_data.get("qty")
        instance.save()
        return instance

    # field level validation

    def validate_price(self,value):
        if value not in range(50,1000):
            raise serializers.ValidationError("invalid price")
        return value

    def validate_qty(self,value):
        if value not in range(5,500):
            raise serializers.ValidationError("invalid qty")
        return value

#object level validation
    # def validate(self,data):
    #     qty=data.get("qty")
    #     price=data.get("price")
    #     if qty not in range(5,500):
    #         raise serializers.ValidationError("invalid qty")
    #     if price not in range(50,1000):
    #         raise serializers.ValidationError("invalid price")
    #     return data







class ReviewSerializer(serializers.ModelSerializer):
    created_date=serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data) #password encrypting method


