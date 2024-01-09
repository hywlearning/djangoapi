from .models import TbMenu,Category
from rest_framework import serializers
from django.contrib.auth.models import User
import bleach


class UserSerializer(serializers.ModelSerializer):   
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email','password')

class CateogrySerializer(serializers.ModelSerializer):
       
    id=serializers.CharField(read_only=True)
    def is_valid(self, raise_exception=False):
        valid = super().is_valid(raise_exception=raise_exception)
        if valid:
            if self.validated_data.get("title") == None:
                valid = False
        return valid
    
    class Meta:
        model=Category
        fields = ['id','title']

class MenuSerializer(serializers.ModelSerializer):
    id=serializers.CharField(source="fd_id",read_only=True)
    price=serializers.CharField(source="fd_price")
    title=serializers.CharField(source="fd_title")
    rating=serializers.CharField(source="fd_inventory")
    #fd_categoryid=serializers.CharField(write_only=True)
    fd_categoryid = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)
    category = serializers.CharField(source='fd_categoryid.title', read_only=True)


    def is_valid(self, raise_exception=False):
        valid = super().is_valid(raise_exception=raise_exception)
        if valid:
            if self.validated_data.get("fd_title") == None:
                valid = True
        return valid
    
    class Meta:
        model = TbMenu
        fields = ['id','title', 'price','rating','category',"fd_categoryid"]
        extra_kwargs = {
            'price':{'min_value':2},
            'rating':{'min_value':0}
        }
    

    
