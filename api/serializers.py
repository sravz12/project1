from rest_framework import serializers
from api.models import Reviews
class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    author=serializers.CharField()
    price=serializers.IntegerField()
    publisher=serializers.CharField()
    qty=serializers.IntegerField()

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


