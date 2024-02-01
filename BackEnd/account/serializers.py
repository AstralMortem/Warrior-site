from rest_framework.serializers import ModelSerializer
from .models import BaseUser,Belt,BeltDescription

class UserListSerializer(ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ['id','full_name','photo', 'is_staff']

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = BaseUser
        fields = "__all__"


        

class BeltListSerializer(ModelSerializer):
    class Meta:
        model = Belt
        fields = "__all__"

class BeltDescriptionSerializer(ModelSerializer):
    class Meta:
        model = BeltDescription
        fields = "__all__"

class BeltDetailSerializer(ModelSerializer):
    description = BeltDescriptionSerializer(many=False, read_only=True)
    class Meta:
        model = Belt
        fields = ['id','code','title','description','photo']